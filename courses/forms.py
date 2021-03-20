from django import forms
from .models import Course
from PIL import Image
from django.forms import ValidationError


class CreateForm(forms.ModelForm):
    slug = forms.SlugField()
    title = forms.CharField(max_length=120)
    description = forms.CharField(widget = forms.Textarea)
    img = forms.ImageField()

    def clean_slug(self):
        data = self.cleaned_data['slug']
        if Course.objects.filter(slug=data):
            raise ValidationError("Этот slug уже используется")

            # Always return the cleaned data, whether you have changed it or
            # not.
        return data

    def clean_title(self):
        data = self.cleaned_data['title']
        if Course.objects.filter(title=data):
            raise ValidationError("Этот title уже используется")

            # Always return the cleaned data, whether you have changed it or
            # not.
        return data


    class Meta:
        model = Course
        fields = ['slug', 'title','description', 'img']
