from django.urls import path

from .views import AddNewsView,NewsListView,EditNewsView,DeleteNewsView,DetailNewsView


urlpatterns = [
    path('add/', AddNewsView.as_view(), name='add_news'),
    path('edit/<int:pk>', EditNewsView.as_view(), name='edit_news'),
    path('delete/<int:pk>', DeleteNewsView.as_view(), name='delete_news'),
    path('detail/<int:pk>', DetailNewsView.as_view(), name='detail_news'),
    path('', NewsListView.as_view(), name='list_news'),
]