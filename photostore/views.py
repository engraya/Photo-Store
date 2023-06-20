from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Caption
from .forms import CaptionForm, EditCaptionForm



# this is a view for listing all the books
def home(request):
    captions = Caption.objects.all()
    context = {'captions' : captions}
    return render(request, 'photostore/home.html', context)


# this is a view for listing a single book,it will take id as an argument
def detail(request, id):
    captions = Caption.objects.get(id=id)
    context = {'captions' : captions}
    return render(request, 'photostore/detail.html', context)


# this is a list for adding a book
def add(request):
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image-file')
        caption = Caption.objects.create(
            title = data['title'],
            continent = data['continent'],
            country = data['country'],
            price = data['price'],
            imageID = data['imageID'],
            image = image
        )

        return redirect('home')
    return render(request, 'photostore/add.html')


def update(request, id):
    caption = Caption.objects.get(id=id)
    form = EditCaptionForm(instance=caption)
    if request.method == 'POST':
        form = EditCaptionForm(request.POST, request.FILES, instance=caption)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'photostore/update.html', context)


# this is a view for deleting a book,it will take id as an argument
def delete(request, id):
    caption = Caption.objects.get(pk=id)
    if request.method == 'POST':
        caption.delete()
        return redirect('home')
    context = {'caption' : caption}
    return render(request, 'photostore/delete.html', context)
