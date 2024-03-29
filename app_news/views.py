from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
# Create your views here.

from .models import News




class AddNewsView(LoginRequiredMixin,CreateView):
    template_name = 'news/add_news.html'
    model = News
    fields = ['news_title','news_description','news_image','content','category']
    success_url = reverse_lazy('list_news')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NewsListView(ListView):
    model = News
    template_name = 'news/list_news.html'


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['news_title','news_description','news_image','content','category']


class EditNewsView(UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'news/edit_news.html'
    success_url = reverse_lazy('list_news')


class DeleteNewsView(DeleteView):
    model = News
    template_name = 'news/delete_news.html'
    success_url = reverse_lazy('list_news')


class DetailNewsView(DetailView):
    model = News
    template_name = 'news/detail_news.html'
    context_object_name = 'news'



