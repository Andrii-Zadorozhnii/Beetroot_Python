
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Company, Manager, User

class RegisterForm(UserCreationForm):
    company_name = forms.CharField(max_length=100)
    manager_phone = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username','password1', 'password2', 'company_name', 'manager_phone']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

        company_name = self.cleaned_data.get('company_name')
        manager_phone = self.cleaned_data.get('manager_phone')
        company = Company.objects.create(company_name=company_name)
        manager = Manager.objects.create(manager_phone=manager_phone, company=company)

        return user