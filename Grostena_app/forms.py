from django import forms
from .models import AutoService, RepairCategory


class AutoServiceForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=RepairCategory.objects.all(),
                                                widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = AutoService
        fields = '__all__'
