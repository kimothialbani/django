from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    subject = forms.CharField(max_length=100)

    def send_email(self):
        print(f"Sending Email from {self.cleaned_data['email']} "
              f"with message: {self.cleaned_data['message'] }")
