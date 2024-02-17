from django.urls import path, re_path
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordChangeDoneView, 
    PasswordChangeView
)

from app.views import (
    main
)


urlpatterns = [
    # login
    path('accounts/login/', LoginView.as_view()),
    path('changepassword/', PasswordChangeView.as_view(
        template_name = 'registration/change_password.html'), name='editpassword'),
    path('changepassword/done/', PasswordChangeDoneView.as_view(
        template_name = 'registration/afterchanging.html'), name='password_change_done'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # files
    path('image/<str:file_name>/', main.get_image),
    path('image/<str:file_name>/<str:folder>/', main.get_image),
    path('upload/<str:folder>/', main.upload_image),
    re_path(r'^files/(?P<path>.*)$', main.get_file),


]
