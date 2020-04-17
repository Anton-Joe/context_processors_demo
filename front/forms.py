from django import forms
from .models import User


class SignUpForm(forms.ModelForm):
    password_repeat = forms.CharField(max_length=20, min_length=2)

    def clean(self):
        cleaned_data = super().clean()
        password_repeat = cleaned_data.get('password_repeat')
        password = cleaned_data.get('password')
        if password != password_repeat:
            raise forms.ValidationError(message='两次密码输入不一致')
        else:
            return cleaned_data

    class Meta:
        model = User
        fields = '__all__'


class SignInForm(forms.ModelForm):
    # {'password': [{'message': '密码长度必须大于3', 'code': 'min_length'}]}
    def get_errors(self):
        new_errors = []
        errors = self.errors.get_json_data()
        for messages in errors.values():
            print(messages)
            for message_dict in messages:
                for key, message in message_dict.items():
                    if key == 'message':
                        new_errors.append(message)
        return new_errors


    class Meta:
        model = User
        fields = ['username', 'password']
        error_messages = {
            'username': {
                'min_length': '用户名长度必须大于2'
            },
            'password': {
                'min_length': '密码长度必须大于3'
            }
        }
