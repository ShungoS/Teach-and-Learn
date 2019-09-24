from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class ReqPost(models.Model):
    title = models.CharField(max_length=100)
    #text data with maximum lenght
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #delete the post if user deleted but not delete user when post deleted.
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('reqpost-detail', kwargs={'pk': self.pk})