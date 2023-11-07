from django import forms

from doit.models import DOITLIST

class DOITLISTForm(forms.ModelForm):
    class Meta:
        model = DOITLIST
        fields = ['subject', 'content', 'create_date', 'done_date', 'is_done']