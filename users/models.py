from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class Mess(models.Model):
    title = models.CharField(max_length=100, default="NO_TOPIC", help_text="Тема письма")
    email = models.EmailField(help_text="Ваша почта")
    message = models.TextField(max_length=1000, help_text="Ваше сообщение")

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
    def get_absolute_url(self):
        return reverse('send')

class Profile(models.Model):
    SEX = (
    ('m','Male'),
    ('f','Female')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('Photo', default='default.png', upload_to='user_images')
    sex = models.CharField(max_length=6, choices=SEX, default='m')
    agreement = models.BooleanField(null=True, blank = True)

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 256 or image.width >256:
            resize = (256,256)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'
