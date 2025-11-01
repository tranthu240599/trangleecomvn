from django.urls import path
from . import views
from .views import upload_image
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', upload_image, name='upload_image'),
    path('upload/delete/<int:id>/', views.delete_image, name='delete_image'),
    path('gioi-thieu/', views.gioi_thieu, name='gioi_thieu'),
    path('tuyen-dung/', views.tuyen_dung, name='tuyen_dung'),
    path('lien-he/', views.lien_he, name='lien_he'),
    path('gui-yeu-cau/', views.lien_he, name='gui_yeu_cau'),
    path('cam-on/', views.cam_on, name='cam_on'),
    path('showroom/', views.showroom, name='showroom'),
    path('showroom-qn/', views.showroom_qn, name='showroom_qn'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


