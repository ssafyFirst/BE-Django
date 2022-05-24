from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data

        user = super().save_user(request, user, form, False)

        profile_img = data.get('profile_img', '')
        if profile_img:
            user.profile_img = profile_img
        
        like_genres = data.get('like_genres', [])
        if like_genres:
            user.like_genres = like_genres

        user.save()

        return user