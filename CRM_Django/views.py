from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm, add_form,update_orders
from .models import Record,Orders
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    record= Record.objects.all()
    Total_orders= Orders.objects.count()
    pending_orders= Orders.objects.filter(Status=0).count()
    Delivered= Orders.objects.filter(Status=1).count()
    Cancelled_orders= Orders.objects.filter(Status= 2).count()
    context= {'Total_orders':Total_orders,
              "pending_orders":pending_orders,
              "Delivered":Delivered,
              "Cancelled_orders":Cancelled_orders,
              "orders":Orders.objects.all().order_by("-Date_ordered"),
              "records":record}
    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']
        user= authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You have succesfully logged In!')
            return redirect('home')
        else:
            messages.success(request,'Username or password is incorrect')
            return redirect('home')
        
    else:
        return render(request,'home.html',context) 
    
#  update_orders
def up_orders(request, pk):
    orders= Orders.objects.get(Order_id= pk)
    form= update_orders(request.POST or None, instance=orders)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                form.save()
                messages.success(request,"Updated Successfully!! ")
                return redirect('home')
            else:
                messages.success(request,form.errors)
    else:
        messages.success(request,"you must be logged in!!  ")
        return redirect('home')
    return render(request,"update_orders.html", {'form':form, "orders":orders})
            

# Create orders
def create_orders(request):
    record= Record.objects.all()
    if request.user.is_authenticated:
        if request.method=="POST":
            Customer= request.POST.get('Customers')
            product_name= request.POST.get('pro_name')
            date= request.POST.get('datetime')
            status= request.POST.get('status')
            if status=="Pending":
                status= 0
            elif status=="Delivered":
                status=1
            elif status=="Cancelled":
                status=2

            try:
                Customer= Customer.split()
                Customer_data= Record.objects.get(first_name= Customer[0])
                Orders.objects.create(Customer_ID= Customer_data, product_name= product_name,Date_ordered= date,Status= status)
                messages.success(request,"Orders Created Successfully!! ")
                return redirect('home')
            except ObjectDoesNotExist:
                messages.success(request, "Please select a Customer... ")
            except ValueError:
                messages.success(request,"Please select Status.... ")

    else:
        messages.success(request, "You must be logged in!! ")
        return redirect('home')
    return render(request,"create_orders.html", {"record":record})  

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
    

# delete record
# def delete_record(request,pk):
#     if request.user.is_authenticated:
#         delete= Record.objects.get(id=pk)
#         delete.delete()
#         return redirect('home')
#     else:
#         messages.success(request,"You must be logged in to do that....")
#         return redirect('home') 
    

def add_record(request):
    form= add_form(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                form.save()
                messages.success(request,"Successfully Added... ")
                return redirect('home') 
            else:
                messages.success(request, form.errors)
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



        
