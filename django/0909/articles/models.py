from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')

    image_thumb = ImageSpecField(
        source='image',             
        processors= [Thumbnail(200, 200)],
        format = 'JPEG',
        options = {
            'quality': 90,
        }
    )

    # image_thumb = ProcessedImageField(
    #     blank=True,
    #     processors = [Thumbnail(200, 200)],
    #     format = 'JPEG',
    #     options = {
    #         'quality': 90,

    #     },
    # )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

