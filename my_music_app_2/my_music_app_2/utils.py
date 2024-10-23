from my_music_app_2.user_profile.models import Profile


def get_user_obj():
    return Profile.objects.first()