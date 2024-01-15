from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm, add_form
from .models import Record


def home(request):
    record= Record.objects.all()
    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']
        user= authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You have succesfully logged In!')
            return redirect('home')
        else:
            messages.success(request,'There was an error logging you in')
            return redirect('home')
        
    else:
        return render(request,'home.html',{'records':record}) 

def logout_user(request):
    logout(request)
    messages.success(request,"You have successfully logged out!") 
    return redirect('home') 

def register_user(request):
    if request.method=="POST":
        form= SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            password= form.cleaned_data['password2']
            user= authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have Successfully Registered")
            return redirect('home')  
    else:
        form= SignUpForm()  
    return render(request,'register.html',{'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record= Record.objects.get(id= pk)
        return render(request, 'record.html',{'Records':customer_record})
    else:
        messages.success(request,"You must be logged in to view that page..")
        return redirect('home') 
    
def delete_record(request,pk):
    if request.user.is_authenticated:
        delete= Record.objects.get(id=pk)
        delete.delete()
        return redirect('home')
    else:
        messages.success(request,"You must be logged in to do that....")
        return redirect('home') 
    

def add_record(request):
    form= add_form(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                addrec= form.save()
                messages.success(request,"Successfully Added... ")
                return redirect('home') 
    else:
        messages.success(request,"You have to log in first... ")
        return redirect('home') 

    return render(request,'add_record.html',{'form':form})

def update_record(request,pk):
    if request.user.is_authenticated:
        record_update= Record.objects.get(id=pk)
        form= add_form(request.POST or None, instance=record_update)
        if form.is_valid():
            form.save()
            messages.success(request,"Record has been successfully updated... ")
            return redirect('home')
    else:
        messages.success(request, "You must be logged in... ")
        return redirect('home')
    
    return render(request,'update_record.html',{'record':record_update,'form':form})



        
