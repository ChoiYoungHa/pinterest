from django.forms import ModelForm

from .models import Profile


# 프로파일 폼 추가
class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']
