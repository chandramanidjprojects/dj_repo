from django import forms
from ajaxapp.models import Student
class StudentForm(forms.ModelForm):
  class Meta:
    model=Student
    fields=['name','marks']
    
  def clean(self):   
      idata=super().clean()
      iname=idata['name']
      imarks=idata['marks']
      if len(iname)<4:
        raise forms.ValidationError('invali name')
      
     
      if imarks<35:
        raise forms.ValidationError('invali marks')
       
     
     