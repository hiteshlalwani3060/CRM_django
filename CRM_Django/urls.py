from django.urls import path
from . import views
urlpatterns=[
    path('', views.home, name='home'),
    path('logout_user/', views.logout_user,name="logout"),
    path('register/',views.register_user,name="register"),
    path('record/<int:pk>/',views.customer_record,name="record"),
    path('delete_record/<int:pk>/',views.delete_record,name="Delete"),
    path('add_record/',views.add_record,name="add"),
    path('update_record/<int:pk>/',views.update_record,name="update")
]