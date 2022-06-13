from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# to User for easy referencing
User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - {self.published_date.date()}"
