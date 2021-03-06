from django import forms
from django.contrib.auth.models import User
from moneykatz.models import File, Category, UserProfile


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, label='Category Name')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)


class FileForm(forms.ModelForm):
    title = forms.CharField(max_length=128, label='Provide a filename',
                            widget=forms.TextInput(attrs={'placeholder': 'File Display Name'}))
    document = forms.FileField(label='Select a File', help_text='max. 42Mb')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = File
        fields = ('title', 'document',)
        # exclude = ('category',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture', 'spirit_animal_picture')


class ContactForm(forms.Form):
    from_email = forms.EmailField()
    subject = forms.CharField(max_length=128, required=True)
    message = forms.CharField(widget=forms.Textarea, max_length=4096, required=True)

    # class Meta:
    #     model = Contact
    #     fields = ('from_email', 'subject', 'message')
