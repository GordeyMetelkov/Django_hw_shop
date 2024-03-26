from django import forms

class EditProductForm(forms.Form):
    product_name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    product_count = forms.IntegerField(initial=0)

class AddImageForm(forms.Form):
    image = forms.ImageField()