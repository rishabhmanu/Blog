from django import forms
from .models import Post
# our new form
class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Your Email', required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)