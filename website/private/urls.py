from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index,name='index'),
    path('reg.html/',views.reg,name='reg'),
    path('',views.home,name='home'),
    path('storedata/',views.storedata,name='storedata'),
    path('send_mail/',views.send_mail,name='send_mail'),
    path('notification/',views.notification,name='notification'),
    path('update_notifications/',views.update_notifications,name='update_notifications'),
    path('stafflogin/',views.stafflogin,name='stafflogin'),
    path('get_notifications/',views.get_notifications,name='get_notifications'),
]