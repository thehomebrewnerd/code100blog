# blogs/models.py
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    post_round = models.PositiveIntegerField(verbose_name='Round')
    post_day = models.PositiveIntegerField(verbose_name='Day')
    title = models.CharField(max_length=200)
    progress = models.TextField()
    thoughts = models.TextField(blank=True, default='')
    work_link = models.CharField(max_length=200, blank=True, default='')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']


    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.title
