from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class BookStore(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Coupon(models.Model):
    coupon_number = models.CharField(max_length=30, primary_key=True)
    usage = models.ForeignKey(BookStore, on_delete=models.CASCADE, null=True, blank=True)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    use_date = models.DateTimeField(max_length=30, null=True, blank=True)
    used = models.BooleanField(default=False)

    def __str__(self):
        return self.coupon_number
