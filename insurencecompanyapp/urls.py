from django.urls import path

from insurencecompanyapp import views 

urlpatterns = [
    path('insurence',views.get_insurence_detailes,name="insurence"),
 
]
