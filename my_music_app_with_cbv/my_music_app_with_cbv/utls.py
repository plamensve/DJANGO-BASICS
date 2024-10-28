from my_music_app_with_cbv.user_profile.models import Profile


def get_user_object():
    return Profile.objects.first()