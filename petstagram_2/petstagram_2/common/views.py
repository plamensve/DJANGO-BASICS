from django.shortcuts import render, redirect

from petstagram_2.common.models import Like
from petstagram_2.photos.models import Photo


def home_page(request):
    all_photos = Photo.objects.all()

    context = {
        'all_photos': all_photos
    }

    return render(request, 'common/home-page.html', context)


def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')