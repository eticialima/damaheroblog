from django.shortcuts import render, redirect
from .models import Category, Photo

# Configurações da galeria e tela inicial
def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)

# Configuração para ver a foto quando clica no botão

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})

# tela do formulario onde adiciona as fotos e fields
def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None

        photo = Photo.objects.create(
            titulo=data['titulo'],
            image=image,
            category=category,
            description=data['description'],

            info_typegame=data['info_typegame'],
            info_datelaunch=data['info_datelaunch'],
            info_designers=data['info_designers'],
            info_developers=data['info_developers'],
            info_publish=data['info_publish'],
            info_genero=data['info_genero'],

            req_processador=data['req_processador'],
            req_memoria=data['req_memoria'],
            req_memoriavideo=data['req_memoriavideo'],
            req_direct=data['req_direct'],
            req_sistema=data['req_sistema'],
            req_volumedisco=data['req_volumedisco'],

            button_mega=data['button_mega'],
            button_media=data['button_media'],
            )

        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'photos/add.html', context)

