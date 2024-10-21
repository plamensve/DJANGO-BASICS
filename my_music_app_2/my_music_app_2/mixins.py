from my_music_app_2.user_profile.models import Profile


class GetProfileObject:
    @staticmethod
    def get_profile_object():
        try:
            return Profile.objects.first()
        except Profile.DoesNotExist:
            return None
