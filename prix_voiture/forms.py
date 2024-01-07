from django import forms
from prix_voiture.models import *


class form_ajout_voiture(forms.ModelForm):
    class Meta:
        model = details_voiture
        exclude = ['']
        widgets = {
            # 'autres': forms.Textarea(attrs={'placeholder': 'details du mot', 'rows': '5', }, ),
        }

    def __init__(self, *args, **kwargs):
        super(form_ajout_voiture, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name == 'boite_vitesse' or visible.name=='carburant':
                visible.field.widget.attrs['class'] = 'form-select'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['id'] = visible.name
