from django.db import models
from django.utils import timezone
from django import forms

class TrangNoiDung(models.Model):
    ten_trang = models.CharField(max_length=100, unique=True)
    tieu_de = models.CharField(max_length=200)
    noi_dung = models.TextField()
    anh_dai_dien = models.ImageField(upload_to='trang/', blank=True, null=True)

    def __str__(self):
        return self.ten_trang

class TrangNoiDungForm(forms.ModelForm):
    class Meta:
        model = TrangNoiDung
        fields = ['ten_trang', 'tieu_de', 'noi_dung', 'anh_dai_dien']

# Các model khác giữ nguyên
class GalleryImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(default=timezone.now)

class SanPham(models.Model):
    ten = models.CharField(max_length=100)
    mo_ta = models.TextField()
    gia = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to='sanpham/')
    noi_bat = models.BooleanField(default=False)

    def __str__(self):
        return self.ten

class SlideImage(models.Model):
    image = models.ImageField(upload_to='slide/')
    mo_ta = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.mo_ta or f"Slide {self.id}"

