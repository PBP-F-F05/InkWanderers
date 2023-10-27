from django.forms import ModelForm
from reviews.models import Review

class ProductForm(ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "review"]