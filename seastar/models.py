from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
# Create your models here.




class Welcome(models.Model):
    author = models.CharField(max_length=100,verbose_name='Yazar')
    title = models.CharField(max_length=500,verbose_name='Başlık')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True,verbose_name='Resim : (535x595)')
    info = RichTextUploadingField()


    def __str__(self):
        return self.author



class Comment(models.Model):
    name =  models.CharField(max_length=150,default='Marka İsmi',verbose_name='Müşteri İsmi')
    info = models.TextField(max_length=250,verbose_name='Müşteri Yorumu')


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True,verbose_name='İsim')
    slug = models.SlugField(max_length=20, db_index=True, unique=True)


    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,verbose_name='Kategori')
    name = models.CharField(max_length=200, db_index=True,verbose_name='İsim')
    list  = models.ImageField(upload_to='products/%y/%m/%d', blank=True,verbose_name='Resim: (500x500)')
    welcome = models.CharField(max_length=10000, db_index=True,verbose_name='İlk Sayfa Açıklaması')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True,verbose_name='Resim: (1500x1000)')
    title = models.CharField(max_length=200, db_index=True,verbose_name='Başlık')
    info = RichTextUploadingField()
    price = models.CharField(max_length=200, db_index=True,verbose_name='Fiyat')
    m2 = models.CharField(max_length=200, db_index=True,verbose_name='Room')
    person = models.CharField(max_length=200, db_index=True,verbose_name='Person')
    minibar = models.CharField(max_length=200, db_index=True,verbose_name='Bar')
    wifi= models.CharField(max_length=200, db_index=True,verbose_name='Wifi')
    heatwater = models.CharField(max_length=200, db_index=True,verbose_name='Heat Water')
    aircon = models.CharField(max_length=200, db_index=True,verbose_name='Aircon')
    shower = models.CharField(max_length=200, db_index=True,verbose_name='Shower')
    tv = models.CharField(max_length=200, db_index=True,verbose_name='Tv')
    info_two = RichTextUploadingField()
    des = models.CharField(max_length=500, default="SEO Description")
    key = models.CharField(max_length=550, default="SEO Keyword için Giriş")
    available = models.BooleanField(default=True)
    facebook = models.CharField(max_length=500, default="Facebook Adresini Giriniz")
    instagram = models.CharField(max_length=500, default="İnstagram Adresini Giriniz")
    slug = models.SlugField(max_length=200, db_index=True)



    def __str__(self):
        return self.name

    def get_absolute_url(self):

        return reverse('product_detail',args=[self.slug , self.id])




class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title


class Restaurant(models.Model):
    no = models.CharField(max_length=200, db_index=True,verbose_name='No')
    list = models.ImageField(upload_to='products/%y/%m/%d', blank=True, verbose_name='Resim: (350x324)')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True, verbose_name='Resim: (1920x1080)')


    def __str__(self):
        return self.no


class Pool(models.Model):
    no = models.CharField(max_length=200, db_index=True, verbose_name='No')
    list = models.ImageField(upload_to='products/%y/%m/%d', blank=True, verbose_name='Resim: (350x324)')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True, verbose_name='Resim: (1920x1080)')

    def __str__(self):
        return self.no

class Gallery(models.Model):
    no = models.CharField(max_length=200, db_index=True, verbose_name='No')
    list = models.ImageField(upload_to='products/%y/%m/%d', blank=True, verbose_name='Resim: (350x324)')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True, verbose_name='Resim: (1920x1080)')

    def __str__(self):
        return self.no