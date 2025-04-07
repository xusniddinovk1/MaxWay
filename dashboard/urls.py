from django.urls import path
from .views import *

urlpatterns = [
    # path('', main_dashboard, name="main_dashboard"),
    path('login/', login_page, name="login_page"),
    path('logout/', logout_page, name="logout_page"),
]
