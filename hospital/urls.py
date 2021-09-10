from django.urls import path
from hospital import views

urlpatterns = [
    # 3 parameters {path + founction_view + dynamic url name }
    path('hospital_data',views.hospital_data_view,name = "hospital_data"),
]