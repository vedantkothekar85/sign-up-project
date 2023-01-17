from django.urls import path
from .import views


urlpatterns = [
    
     path('test/',views.test, name='test'),   
    
    
    # login form urls
    path('',views.signup,name="signup"),
    path('login/',views.login, name="login"),
    
]
