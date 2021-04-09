from django.db import models

# Create your models here.


class BlogPost(models.Model):
    # Reddit, Twitter, Youtube, etc.
    post_id = models.CharField(
        max_length=250, null=True, blank=True, unique=True)
    post_title = models.CharField(max_length=200, null=True, blank=True)
    item_text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.post_title

        # Create Tweet and Reddit posts as models, because they will be stored as DB info
