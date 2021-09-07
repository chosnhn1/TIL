from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)                 # User input, Class variable
    content = models.TextField()                            # User input
    created_at = models.DateTimeField(auto_now_add=True)    # Auto-filled by django
    updated_at = models.DateTimeField(auto_now=True)        # Auto-filled by django

    def __str__(self):
        return f'Post #{self.pk}: {self.title}'