from django import forms

class write_your_post(forms.Form):
    from_someone = forms.CharField(max_length=20, label="From")
    to_someone = forms.CharField(max_length=20, label="To")
    message = forms.CharField(max_length=120, required=True, label="Message")


