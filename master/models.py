
from django.db import models
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save

from account.serializers import User


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, primary_key=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

@receiver(pre_save, sender=Category)
def product_pre_save(sender, instance, *args, **kwargs):
     if not instance.slug:
        instance.slug = slugify(instance.name)


class Master(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='masters')
    image = models.ImageField(upload_to='images/',
                              null=True, blank=True)
    ot = models.TimeField()
    do = models.TimeField()

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return f'{self.name} - {self.description}'

class Comment(models.Model):
    owner = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    master = models.ForeignKey(Master, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.owner} -> {self.master} -> {self.created_at}'


class Likes(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked')

    class Meta:
        unique_together = ['master', 'user']


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='favorites')




