from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Categories(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'
        db_table = 'categories'


class News(models.Model):
    news_title = models.CharField(max_length=255)
    news_description = models.CharField(max_length=255)
    news_image = models.ImageField(upload_to='news')
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name_plural = 'News'
        db_table = 'news'