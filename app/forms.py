from django import forms





def check_for_b(value):
    if value[0].lower()=='b':
        raise forms.ValidationError('name is started with b')
    
def check_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('length is less than 5 characters')


class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_b,check_for_len])
    sid=forms.IntegerField()
    age=forms.IntegerField()
    email=forms.EmailField()
