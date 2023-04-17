from django.shortcuts import render, get_object_or_404, redirect

from seastar.models import Welcome, Product, Comment, Images, Restaurant, Pool, Gallery
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.



def index(request):



    welcomes = Welcome.objects.all()
    important = Product.objects.filter(category__name__icontains='İmportant')
    favorite = Product.objects.filter(category__name__icontains='Favorite')
    rooms = Product.objects.all()
    comments = Comment.objects.all()



    context = {
        'welcomes':welcomes,
        'important':important,
        'favorite':favorite,
        'rooms':rooms,
        'comments':comments
    }

    return render(request,'central/index.html',context)



def detail(request,slug,id):
    rooms = Product.objects.all()
    product = get_object_or_404(Product, slug=slug, id=id, available=True)
    images = Images.objects.filter(product_id=id)



    context = {
        'product':product,
        'images':images,
        'rooms':rooms
    }

    return render(request,'central/detail.html',context)



def about(request):
    rooms = Product.objects.all()
    welcomes = Welcome.objects.all()



    context = {
        'welcomes':welcomes,
        'rooms':rooms
    }
    return render(request,'central/about.html',context)


def contact(request):
    rooms = Product.objects.all()

    if 'btnSubmit' in request.POST:
        if True:
            name = request.POST.get('name')
            email = request.POST.get('email')

            message = request.POST.get('message')


            subject = 'Costumer Contact Messages'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email,"djangomarmaris@gmail.com"]
            contact_message = "Name:%s\nEmail:%s\nPhone:%s" % (
                name,
                email,

                message,
            )
            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)

            if request.LANGUAGE_CODE == 'en':
                messages.success(request, 'Thank you, your request has been received.')
            else:
                messages.success(request, 'Teşekkürler isteğiniz tarafımıza ulaştı.')

        return redirect('/')

    context = {
        'rooms':rooms
    }
    return render(request,'central/contact.html',context)



def restaurant(request):
    rooms = Product.objects.all()

    product = Restaurant.objects.all()



    context ={
        'product':product,
        'rooms':rooms
    }

    return render(request,'central/restaurant.html',context)


def pool(request):
    rooms = Product.objects.all()
    product = Pool.objects.all()



    context = {
        'product':product,
        'rooms':rooms
    }

    return render(request,'central/pool.html',context)



def gallery(request):
    rooms = Product.objects.all()

    product = Gallery.objects.all()

    context = {
        'product': product,
        'rooms':rooms
    }


    return render(request,'central/gallery.html',context)