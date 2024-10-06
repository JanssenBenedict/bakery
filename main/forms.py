from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "category", "quantity"]

    def clean_name(self):
        return strip_tags(self.cleaned_data["name"])
    
    def clean_category(self):
        return strip_tags(self.cleaned_data["category"])
    
    def clean_description(self):
        return strip_tags(self.cleaned_data["description"])