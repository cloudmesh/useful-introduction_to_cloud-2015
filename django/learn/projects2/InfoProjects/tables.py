import django_tables2 as tables
from InfoProjects.models import InfoProject


#class PersonTable(tables.Table):
        #name = tables.Column(verbose_name = "full name")

class NameTable(tables.Table):
        project_title = tables.Column()
        project_id = tables.Column()
        project_pi = tables.Column()
        project_description = tables.Column()
        code = tables.Column()
        
       class Meta:
        model = InfoProject
        attrs = {"class": "paleblue"}
