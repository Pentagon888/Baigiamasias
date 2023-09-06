from django import forms
from .models import AutoService, RepairCategory


class AutoServiceForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=RepairCategory.objects.all(),
                                                widget=forms.CheckboxSelectMultiple)

    class Meta:
        error_messages = {
            "name": {
                "required": "Šitas laukas yra privalomas.",
            },
            "category": {
                "required": "Šitas laukas yra privalomas.",
            },
            "location_lat": {
                "required": "Šitas laukas yra privalomas.",
            },
            "location_lon": {
                "required": "Šitas laukas yra privalomas.",
            },
            "address": {
                "required": "Šitas laukas yra privalomas.",
            }, "phone_number": {
                "required": "Šitas laukas yra privalomas.",
            },
            "working_hours": {
                "required": "Šitas laukas yra privalomas.",
            },
            "working_hours": {
                "required": "Šitas laukas yra privalomas.",
            }

        }
        model = AutoService
        fields = '__all__'
