from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from products.views import HomePage, product_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view()),
    path('products/<int:id>', product_page)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)