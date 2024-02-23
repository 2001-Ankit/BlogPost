from django import forms
from .models import BlogPost
from .models import Category

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'description', 'image', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs['class'] = 'form-control'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','slug']


