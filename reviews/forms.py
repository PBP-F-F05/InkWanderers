from django.forms import ModelForm
from reviews.models import Review
from django import forms

class ProductForm(ModelForm):
    RATING_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )
    rating = forms.ChoiceField(
        label="Rating",
        choices=RATING_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Review
        fields = ["rating", "review"]