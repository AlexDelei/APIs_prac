"""
writing regular django views using our serializer

Implementing some API views using our new Serializer class
"""
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view # function based
from rest_framework.response import Response
from rest_framework import status
from snippets.models import Snippets
from snippets.serializers2 import SnippetsSerializer


@api_view(['GET', 'POST']) 
def snippet_list(request, format=None):
    """
    List of all code snippets, or create a new snippet
    """
    if request.method == 'GET': # get request method
        snippets = Snippets.objects.all() # query from database/storage engine
        serializer = SnippetsSerializer(snippets, many=True) # serializing data from storage to be jsonified
        return Response(serializer.data) # returning a json response of the serialized data
    
    if request.method == 'POST': # post request method
        serializer = SnippetsSerializer(data=request.data) # serializing the post data before storing it
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # return serialized data from a successful post request
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST) # otherwise there is an error


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippets.objects.get(pk=pk)
    except Snippets.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SnippetsSerializer(snippet)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = SnippetsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method =='DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)