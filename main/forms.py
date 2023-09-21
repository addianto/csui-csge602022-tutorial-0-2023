from django.forms import ModelForm

from main.models import Product


# pylint: disable=too-few-public-methods
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]
