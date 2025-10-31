from django.shortcuts import render, redirect
from .models import  GalleryImage
from django.core.mail import send_mail

def home(request):
    images = GalleryImage.objects.all()
    return render(request, 'home.html', {'images': images})

#-----------GIỚI THIỆU--------------------
def gioi_thieu(request):
    return render(request, 'gioi-thieu.html')
def gioi_thieu_view(request):
    return render(request, 'trang_chu.html', {'active_section': 'gioi_thieu'})
def tuyen_dung(request):
    return render(request, 'tuyen-dung.html', {'active_section': 'tuyen_dung'})
def lien_he(request):
    if request.method == 'POST':
        ho_ten = request.POST['ho_ten']
        email = request.POST['email']
        sdt = request.POST['so_dien_thoai']
        noi_dung = request.POST['noi_dung']
        send_mail(
            subject=f"Yêu cầu từ {ho_ten}",
            message=f"SĐT: {sdt}\nEmail: {email}\n\nNội dung:\n{noi_dung}",
            from_email='web@tranglee.vn',
            recipient_list=['lienhe@tranglee.vn'],
        )
        return redirect('cam_on')
    return render(request, 'lien-he.html', {'active_section': 'lien_he'})











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


