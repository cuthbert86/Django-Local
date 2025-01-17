from rest_framework.serializers import ModelSerializer , ReadOnlyField 
from itreporting.models import Issue 


class IssueSerializer(ModelSerializer): 

    author = ReadOnlyField(source = 'author.username') 

    class Meta:

        model = Issue 

        fields = [
            'type', 'room', 'urgent', 'details', 'date_submitted', 'author']
