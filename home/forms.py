from django.forms import ModelForm
from .models import Registration

class RegistrationForm(ModelForm):
    class Meta:
        model= Registration
        exclude= ('creat_at', 'last_modified_at', 'ipAddress')
