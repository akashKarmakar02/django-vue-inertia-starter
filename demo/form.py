from django.forms import ModelForm

from demo.models import Test


class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = '__all__'
