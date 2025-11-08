from django import forms
from .models import TrangNoiDung

class TrangNoiDungForm(forms.ModelForm):
    class Meta:
        model = TrangNoiDung
        fields = ['ten_trang', 'tieu_de', 'noi_dung', 'anh_dai_dien']
