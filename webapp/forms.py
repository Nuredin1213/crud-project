from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from.models import Record
from django.forms.widgets import PasswordInput,TextInput





#register/create user
class CreateUserForm(UserCreationForm):
    class Meta:
        model =User #it will be saved to this model database
        fields = ['username','password1','password2'] # we set the attributes as went here not from the model


#crate log in form

class LoginForm(AuthenticationForm):#we create fields recies as post and authencate and redirect to neccery  we authenticate aregen redirect wedemifelegew neger in login functional
    username = forms.CharField(widget=TextInput())#model ersu yelewm
    password = forms.CharField(widget=PasswordInput())

# create a record
class createRecordFORM(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'
        exclude = ['created_at','author'] #since create autho silemimola and author also berasu as we did the functionality in views


# update a record
class UpdateRecordFORM(forms.ModelForm): 
    class Meta:
        model = Record
        fields = '__all__'
        exclude = ['created_at',] # the same form as createrecordform