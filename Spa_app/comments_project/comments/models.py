from django.db import models
from django.utils import timezone


class Comment(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    homepage = models.URLField(blank=True, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    user_ip = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.username}-{self.email}'


class Attachment(models.Model):
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def is_image(self):
        return self.file.name.lower().endwith(('.png','.jpg','.jpeg','.gif'))


class Captcha(models.Model):
    key = models.CharField(max_length=10, unique=True)
    text = models.CharField(max_length=10)
    image = models.ImageField(upload_to='captcha/')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.key