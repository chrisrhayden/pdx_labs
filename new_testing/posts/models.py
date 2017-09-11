import re
import string
from django.db import models
from django.utils import timezone


# Create your models here.


class BlogPost(models.Model):

    text = models.TextField()
    author = models.CharField(max_length=100,
                              blank=True, null=False)
    created = models.DateTimeField(timezone.now())
    title = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.author is None:
            self.author = 'Anon'
        super().save(*args, **kwargs)

    def get_excerpt(self):
        sum_text = self.text.split('\n')
        # small = [line.replace('\n', '') for line in sum_text]
        small = ''.join(sum_text[:3])
        return small


class Comment(models.Model):

    text = models.TextField()
    author = models.CharField(max_length=100)
    post_parent = models.ForeignKey(BlogPost)

    def __str__(self):
        return self.text
