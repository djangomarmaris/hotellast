"""hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns
from seastar import views



urlpatterns = [
    path('i18n/',include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),

]
urlpatterns += i18n_patterns (
    path('', views.index, name='index'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('<str:slug>/<int:id>', views.detail, name='product_detail'),
    path('about/', views.about, name='about'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('pool/', views.pool, name='pool'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
)
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)