from django.urls import path
from authap.views import login, logout
app_name = 'authap'
urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
