from django.contrib import admin
from .models import Record,Interactions,Tasks,Opportunities,Orders

admin.site.register(Record)
admin.site.register(Interactions)
admin.site.register(Tasks)
admin.site.register(Opportunities)

class orders(admin.ModelAdmin):
    list_display= ('Customer_ID','product_name','Status','Date_ordered')

admin.site.register(Orders,orders)

