from django.db import models
from django.utils import timezone


STATUS= (
    (0,"Pending"),
    (1,"Completed"),
    (2,'In_progress')
)
STATUS2= (
    (0,"Pending"),(1,"Delivered"),(2,"Cancelled")
)
PRIORITY= (
    (0,'Low'),
    (1,'Medium'),
    (2,'High'),
)
TYPE= (
    (0,'Call'),
    (1,'Email'),
    (2,'meeting'),
)

DEAL= (
    (0,"Prospecting"),(1,"Negotiation"),(2,"Closed-Won"),(3,"Closed-Lost")
)

class Record(models.Model):
    created_at= models.DateTimeField(auto_now_add=True)
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=60)
    email= models.CharField(max_length=100)
    phone= models.IntegerField()
    address= models.CharField(max_length=100)
    city= models.CharField(max_length=50)
    state= models.CharField(max_length=50)
    zipcode= models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name}"
    
class Tasks(models.Model):
    Task_ID= models.IntegerField(primary_key=True,auto_created=True)
    Customer_id= models.ForeignKey(Record, on_delete=models.PROTECT)
    Subject= models.CharField(max_length=300)
    DueDate= models.CharField(max_length=50)
    Status= models.IntegerField(choices=STATUS)
    Priority= models.IntegerField(choices=PRIORITY)
    Notes= models.CharField(max_length=100,default="")
    Date_Created= models.DateField(auto_now_add=True)
    Date_Completed= models.CharField(max_length=50, default="N/A")

    def __str__(self):
        return f"{self.Customer_id} {self.Status}"
    

class Interactions(models.Model):
    Interaction_ID= models.IntegerField(primary_key=True,auto_created=True)
    Customer_ID= models.ForeignKey(Record, on_delete=models.PROTECT)
    Date_Time= models.DateTimeField(auto_now_add=True)
    Type= models.IntegerField(choices=TYPE)

    def __str__(self):
        return f"{self.Customer_ID} {self.Type}"

class Opportunities(models.Model):
    Opportunity_ID= models.IntegerField(primary_key=True,auto_created=True)
    Customer_ID= models.ForeignKey(Record,on_delete=models.PROTECT)
    Deal_Name= models.CharField(max_length=100)
    Stage= models.IntegerField(choices=DEAL)
    Expected_close_date= models.CharField(max_length=40)
    Notes= models.CharField(max_length=30,default="")

    def __str__(self):
        return f"{self.Customer_ID} {self.Deal_Name}"

class Orders(models.Model):
    Order_id= models.IntegerField(primary_key=True, auto_created=True)
    Customer_ID= models.ForeignKey(Record, on_delete=models.PROTECT)
    product_name= models.CharField(max_length=110)
    Date_ordered= models.DateField()
    Status= models.IntegerField(choices=STATUS2) 

    def save(self, *args,**kwargs):
        if not self.Date_ordered:
            self.Date_ordered= timezone.now()
        return super().save(*args, **kwargs)

    





