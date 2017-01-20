from django.forms import ModelForm
from provision.models import Box

class AddBoxForm(ModelForm):
    class Meta:
        model = Box
        fields = '__all__'