from django import forms
from .models import Combo

class ComboForm(forms.ModelForm):
	class Meta:
		model = Combo
		fields = ('file','lowerbound','upperbound')