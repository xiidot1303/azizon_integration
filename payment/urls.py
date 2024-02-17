from django.urls import path, re_path
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordChangeDoneView, 
    PasswordChangeView
)

from payment.views import (
    payme
)

urlpatterns = [
    path('payme/endpoint', payme.endpoint),
]
