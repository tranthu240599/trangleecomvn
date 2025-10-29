from django.shortcuts import render, redirect
from .models import  GalleryImage

def home(request):
    images = GalleryImage.objects.all()
    return render(request, 'home.html', {'images': images})
def gioi_thieu(request):
    return render(request, 'gioi-thieu.html')
def gioi_thieu_view(request):
    return render(request, 'trang_chu.html', {'active_section': 'gioi_thieu'})

def su_kien_view(request):
    return render(request, 'trang_chu.html', {'active_section': 'su_kien'})

def lien_he_view(request):
    return render(request, 'trang_chu.html', {'active_section': 'lien_he'})


#-----------------------Thêm sdile ảnh--------------------
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        GalleryImage.objects.create(image=image_file)
        return redirect('upload_image')
    images = GalleryImage.objects.all()
    return render(request, 'upload.html', {'images': images})
def delete_image(request, id):
    if request.method == 'POST':
        img = GalleryImage.objects.get(id=id)
        img.delete()
    return redirect('upload_image')


