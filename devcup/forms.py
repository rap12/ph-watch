from django import forms

from models import Project

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		exclude = ('contractor','usercontributed','budget','progress','start_date','end_date',)