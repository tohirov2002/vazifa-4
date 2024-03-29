from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('news/', include('app_news.urls')),
    path('', include('app_pages.urls')),
]
