from django.urls import path
from baseapp import views

urlpatterns = [
    path('',views.index,name = "index"),
    path('allmodels/',views.all_model_quires,name = "all_models"),
    path('contact/',views.contact_view,name = "conatct"),
    path('contactsmodel/',views.ContactModelForm_view,name = "conatctModel"),
]