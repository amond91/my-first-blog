from django import forms
from .models import Post, Coupon, BookStore


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ('usage', 'phone_number',)
