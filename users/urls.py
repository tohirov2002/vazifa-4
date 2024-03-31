from django.urls import path

from .views import register_view,login_view,logout_view,email_view

urlpatterns = [
    path('register/', register_view, name='register_page'),
    path('login/', login_view, name='login_page'),
    path('email/', email_view, name='email_page'),
    path('logout/', logout_view, name='logout')
]