from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    #text data with maximum lenght
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #delete the post if user deleted but not delete user when post deleted.
    file = models.FileField('Class Video', upload_to='media/', null=True, blank=True)
    thumbnail = models.ImageField(default='defaultthumb.jpg', upload_to='thunbnail_pics')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    
