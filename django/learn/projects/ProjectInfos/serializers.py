from django.forms import widgets
from rest_framework import serializers
from ProjectInfos.models import ProjectInfo


class ProjectInfoSerializer(serializers.Serializer):
	project_title = serializers.CharField(required=False,
                                  max_length=200)
        project_id = serializers.CharField(required=False,
                                  max_length=200)
        project_pi = serializers.CharField(required=False,
                                  max_length=200)
        project_description= serializers.CharField(widget=widgets.Textarea,
                                 max_length=100000)

def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.project_title = attrs.get('project_title', instance.project_title)
            instance.project_id = attrs.get('project_id', instance.project_id)
            instance.project_pi = attrs.get('project_pi', instance.project_pi)
            instance.project_description = attrs.get('project_description',instance.project_description)
            return instance

        # Create new instance
        return ProjectInfo(**attrs)
