from django.shortcuts import render


def astro_images(request):
    return render(request, 'sky/astro_images.html')

def astro_view(request):
    return render(request, 'sky/astro_view.html')