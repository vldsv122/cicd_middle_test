from django.shortcuts import render, get_object_or_404
from . models import Image
import datetime

def gallery_view(request):
    existring_photos = [
        "1.jpg",
        "2.jpg",
    ]
    pictures_obj = []
    for photo in existring_photos:
        new_obj = Image()
        new_obj.title = f"Name: {photo}"
        new_obj.image = photo
        pictures_obj.append(new_obj)
    
    pictures_obj[0].created_date = datetime.datetime.now() - datetime.timedelta(days=1)
    pictures_obj[1].created_date = datetime.datetime.now() - datetime.timedelta(days=32)
    
    filtered_pictures = []
    for picture in pictures_obj:
        if picture.created_date > datetime.datetime.now() - datetime.timedelta(days=30):
            filtered_pictures.append(picture)
    
    print (filtered_pictures)

    context = {
        "images": filtered_pictures,
    }

    return render(request, 'gallery.html', context)


def image_detail(request, pk):
    photo_id = pk

    photo_obj = Image()
    photo_obj.title = f"Name: {photo_id}"
    photo_obj.image = f"{photo_id}.jpg"
    photo_obj.created_date = datetime.datetime.now() - datetime.timedelta(days=1)

    context = {
        "image": photo_obj,
    }

    return render(request, 'image_detail.html', context)

