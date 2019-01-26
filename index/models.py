from django.db import models

class slider(models.Model):
    category=models.CharField(max_length=150, null=True)
    details=models.CharField(max_length=250, null=True)
    model_pic = models.ImageField(upload_to='static/assets/sliderImages', default='static/assets/img/slider1.jpg')

    def __str__(self):
        return self.category