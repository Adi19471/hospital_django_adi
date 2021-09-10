from django .urls import path 

from userapp import views 

urlpatterns = [
    path('registration_page/',views.userlogin,name="userregistration"),
    path('login/',views.login_view,name="login"),
    path('logouts/',views.logout_view,name="logoutss"),
]
