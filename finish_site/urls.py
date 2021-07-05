
from django.urls import path
from finish_site import views

urlpatterns = [
    path('',views.index , name = 'home'),
    path('welcom',views.welcom, name = 'welcom' )

]