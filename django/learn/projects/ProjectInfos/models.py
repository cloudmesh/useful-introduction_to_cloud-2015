from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Create your models here.

LEXERS = [item for item in get_all_lexers() if item[1]]

class ProjectInfo(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	project_title = models.CharField(max_length = 200, blank=True, default='')
	project_id = models.CharField(max_length = 200, blank=True, default='')
	project_pi = models.CharField(max_length = 200, blank=True, default='')
	project_description = models.TextField()
	
	class Meta:
		ordering = ('created',)
		

