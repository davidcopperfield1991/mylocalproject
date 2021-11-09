from django import forms

class TimeData(forms.Form):
    time = forms.TimeField(
        widget=forms.TextInput
    )
    title = forms.CharField(
        widget=forms.TextInput

    )


class ReportForm(forms.Form):
    job = forms.CharField(
        widget=forms.TextInput(),
        label="job"
    )