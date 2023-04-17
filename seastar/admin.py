from django.contrib import admin
from .models import  Welcome , Category , Product , Restaurant , Pool ,Gallery ,Comment ,Images
# Register your models here.


class JPG(admin.TabularInline):
    model = Images


class WelcomeAdmin(admin.ModelAdmin):
    list_display = ['author']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}

class ProdcutAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
    inlines = (JPG,)


class RestAdmin(admin.ModelAdmin):
    list_display = ['no']


class PoolAdmin(admin.ModelAdmin):
    list_display = ['no']


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['no']



class CommentAdmin(admin.ModelAdmin):
    list_display = ['name']



admin.site.register(Comment,CommentAdmin)
admin.site.register(Product,ProdcutAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Welcome,WelcomeAdmin)
admin.site.register(Restaurant,RestAdmin)
admin.site.register(Pool,PoolAdmin)
admin.site.register(Gallery,GalleryAdmin)

admin.site.site_title = 'Central Web Agency'
admin.site.site_header = 'MARTAS'