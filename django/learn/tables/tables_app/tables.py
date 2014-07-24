import django_tables2 as tables
from tables_app.models import Person


class PersonTable(tables.Table):
    name = tables.Column(verbose_name = "full name")

    class Meta:
        model = Person
	attrs = {"class": "paleblue"}

class NameTable(tables.Table):
    label = tables.Column()
    cm_id = tables.Column()
    summary = tables.Column()
    host = tables.Column()
    user = tables.Column()
    project = tables.Column()
    start_time = tables.Column()
    end_time = tables.Column()
