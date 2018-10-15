from django import forms
from MyFileUploadApp.models import Document


class DocumentForm(forms.ModelForm):
    class Meta():
        model = Document
        fields = ('name','pic',)
