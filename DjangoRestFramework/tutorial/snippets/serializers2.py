"""
Serializing provides a way a representing data in a json format
"""
from rest_framework import serializers
from snippets.models import Snippets, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetsSerializer(serializers.ModelSerializer):
    """
    refactoring the serializer using the ModelSerializer class
    
    ModelSerializer does not do anythin particularly magical, they are simple a shortcut
    for creating serializer classes:
        -> An automatically determined set of fields.
        -> Simple default implementations for the create() and update() methods
    """
    class Meta:
        model = Snippets
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']