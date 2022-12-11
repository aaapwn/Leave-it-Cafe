from django import forms
from .models import Post

class write_your_post(forms.ModelForm):
    from_someone = forms.CharField(required=False)
    to_someone = forms.CharField(required=False)
    class Meta:
        model = Post
        fields = ['from_someone', 'to_someone', 'message']
        labels = {
            'from_someone' : 'From',
            'to_someone' : 'To',
            'message' : 'Message'
        }
