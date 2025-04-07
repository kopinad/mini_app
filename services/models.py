from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    dano = models.TextField()
    zadacha = models.TextField()
    sdelano1 = models.TextField()
    sdelano2 = models.TextField()
    sdelano3 = models.TextField()
    img1 = models.CharField(max_length=255)
    img2 = models.CharField(max_length=255)
    img3 = models.CharField(max_length=255)
    img4 = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='services')

    def str(self):
        return self.name


class Review(models.Model):
    image_path = models.CharField(max_length=255)

    def __str__(self):
        return f"Отзыв #{self.id}"
