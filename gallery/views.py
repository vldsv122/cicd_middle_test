from django.shortcuts import render, get_object_or_404


def gallery_view(request):
    # Return simple response
    return render(request, 'gallery.html')

def image_detail(request, pk):
    # Return simple response
    return render(request, 'image_detail.html')

