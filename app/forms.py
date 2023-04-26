from django import forms
from django.core import validators




def check_for_b(value):
    if value[0].lower()=='b':
        raise forms.ValidationError('name is started with b')
    
def check_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('length is less than 5 characters')


class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_b,check_for_len])
    #sid=forms.IntegerField()
    age=forms.IntegerField()
    email=forms.EmailField()
    re_enter_emial=forms.EmailField()
    mobile=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9\d{9}]')])
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)


    def clean(self):
        e=self.cleaned_data["email"]
        r=self.cleaned_data["re_enter_emial"]
        if e!=r:
            raise forms.ValidationError('not matched')
        
    #def clean_age(self):
    #   a=self.cleaned_data["age"]
    #    if a<6:
    #       raise forms.ValidationError('age is less than 6')



    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('botcatchers are hacked your data base')

        
