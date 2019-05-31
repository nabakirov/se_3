from django.contrib.auth.forms import UserChangeForm as _UserChangeForm


class UserChangeForm(_UserChangeForm):
    class Meta:
        fields = ('username', 'is_staff', 'is_active')
