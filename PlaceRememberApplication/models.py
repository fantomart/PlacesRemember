from django.db import models
from django.contrib.auth.models import User

class Remember(models.Model):
    name = models.CharField(max_length = 100, verbose_name="Название воспоминания")
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField("Фото", upload_to="PlaceRememberApplication/photos", default="", blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    #latitude = models.DecimalField(max_digits=6, decimal_places=3, default=-25.344, verbose_name="Широта", blank= True)
    #longitude = models.DecimalField(max_digits=6, decimal_places=3, default=131.036, verbose_name="Долгота", blank= True)

    latitude = models.CharField(max_length = 100)
    longitude = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Воспоминание"
        verbose_name_plural = "Воспоминания"

    def __str__(self):
        return self.name

