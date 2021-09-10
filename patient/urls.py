from django.urls import path

from patient import views 

urlpatterns = [
    path('',views.Patient_view,name="patient_urls"),
    # url ides dispaly id base conver to int
    
    #path('patient/<int:id>/',views.Patient_detailes,name="fulldetailes"),
    # url based into string base or slug based 
    #path('patient/<str:nameslug>/',views.Patient_detailes,name="fulldetailes"),
    path('patient/<slug:nameslug>/',views.Patient_detailes,name="fulldetailes"),
    #path('patient/<int:id>/',views.Patient_detailes,name="fulldetailes"),
]
