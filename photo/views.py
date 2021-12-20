from django.shortcuts import render,redirect
from .models import Category, Photo


def gallery(request):
    category=request.GET.get('category')
    if category==None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    # photos = Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photo/gallery.html', context)


def add(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])

        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])

        else:
            category = None

        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image
        )
        return redirect('gallery')
    context = {'categories': categories}

    return render(request, 'photo/add.html', context)


def view_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    return render(request, 'photo/view_photo.html', {'photo': photo})
