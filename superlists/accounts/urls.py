from accounts import views
from django.urls import path


urlpatterns = [
    path('send_login_email', views.send_login_email, name='send_login_email'),
]
