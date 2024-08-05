from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()


class ProductStockForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['productStock']