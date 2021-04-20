from django.db import models
# import tweets.py and reddit.py to do api calls

# Create your models here.


class Post(models.Model):
    post_type = models.CharField(
        max_length=20, null=True, blank=True, unique=True)


class BlogPost(models.Model):
    # Reddit, Twitter, Youtube, etc.
    post_id = models.CharField(
        max_length=250, null=True, blank=True, unique=True)
    post_title = models.CharField(max_length=200, null=True, blank=True)
    item_text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.post_title


class Product(models.Model):
    title = models.CharField(max_length=120),
    description = models.TextField(blank=True, null=True),
    price = models.DecimalField(decimal_places=2, max_digits=1000),
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField()

    # Create Tweet and Reddit posts as models, because they will be stored as DB info
