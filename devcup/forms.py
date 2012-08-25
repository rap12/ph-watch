from django import forms

from models import Project

class ProjectForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ProjectForm, self).__init__(*args, **kwargs)
		#self.fields['usercontributed'] = 1

	class Meta:
		model = Project
		exclude = ('contractor','usercontributed','budget','progress','start_date','end_date',)