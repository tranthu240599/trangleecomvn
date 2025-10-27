from django.shortcuts import render, redirect
from .models import  GalleryImage

def home(request):
    images = GalleryImage.objects.all()
    return render(request, 'home.html', {'images': images})


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


