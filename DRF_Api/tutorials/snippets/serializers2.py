"""
Serializing provides a way a representing data in a json format
"""
from rest_framework import serializers
from snippets.models import Snippets, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class SnippetsSerializer(serializers.ModelSerializer):
    """
    refactoring the serializer using the ModelSerializer class
    
    ModelSerializer does not do anythin particularly magical, they are simple a shortcut
    for creating serializer classes:
        -> An automatically determined set of fields.
        -> Simple default implementations for the create() and update() methods
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    # This field `owner` is doing sth interesting. The `source` argument controls which attribute is used to
    # populate a field, and can point at any attribute on the serialized instance. 
    class Meta:
        model = Snippets
        fields = ['id', 'owner', 'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.ModelSerializer):
    """
    UserSerializer ; adding endpoints for the User models

    args:
        serializers.ModelSerializer - c
    """
    queryset = Snippets.objects.all()
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=queryset)

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']