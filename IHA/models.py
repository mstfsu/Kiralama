from django.db import models
from base.models import BaseModel
# Create your models here.

class Category(BaseModel):
    name = models.TextField()
    slug = models.SlugField(unique=True, max_length=500, default="")

class Brand(BaseModel):
    name = models.CharField(max_length=100, verbose_name="Marka Adı")
    description = models.TextField(verbose_name="Marka Açıklaması")
   
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Marka"
        verbose_name_plural = "Markalar"

class IHA(BaseModel):
    name = models.CharField(max_length=100, verbose_name="İHA Adı")
    model_number = models.CharField(max_length=100, verbose_name="İHA Model Numarası")
    description = models.TextField(verbose_name="İHA Açıklaması")
    weight = models.FloatField(verbose_name="İHA Ağırlığı")
    image = models.ImageField(upload_to="iha_images", verbose_name="İHA Resmi", null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Marka")
    category = models.ManyToManyField(Category, verbose_name="Kategori")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Iha"
        verbose_name_plural = "Insansiz Hava Araçları"
        ordering = ["-created_at"]