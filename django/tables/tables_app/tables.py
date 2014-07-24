import django_tables2 as tables
from tables_app.models import Person


class PersonTable(tables.Table):
    name = tables.Column(verbose_name = "full name")

    class Meta:
        model = Person
	attrs = {"class": "paleblue"}

class NameTable(tables.Table):
    name = tables.Column()
    ID = tables.Column()
