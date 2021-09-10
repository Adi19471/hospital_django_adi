from django.urls import path

from claimsapp import views 

urlpatterns = [
    path('claims',views.get_claims_data,name="claim"),
 
]
