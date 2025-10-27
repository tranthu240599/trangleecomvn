from django.urls import path
from . import views
from .views import upload_image,delete_image
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', upload_image, name='upload_image'),
    path('upload/delete/<int:id>/', views.delete_image, name='delete_image')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


