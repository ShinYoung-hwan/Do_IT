from django import forms

from doit.models import DOITLIST

class DOITLISTDetailForm(forms.ModelForm):
    class Meta:
        model = DOITLIST
        fields = ['subject', 'content', 'create_date', 'done_date', 'is_done']
        
        labels = {
            'subject': '제목',
            'content': '내용',
            'create_date': '생성일자',
            'done_date': '완료일자',
            'is_done': '완료 여부'          
        }
        
class DOITLISTCreateForm(forms.ModelForm):
    class Meta:
        model = DOITLIST
        fields = ['subject', 'content', 'done_date']
        
        labels = {
            'subject': '제목',
            'content': '내용',
            'done_date': '완료일자',      
        }