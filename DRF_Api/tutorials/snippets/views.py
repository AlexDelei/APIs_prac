"""
writing regular django views using our serializer

Implementing some API views using our new Serializer class
"""
##################################################
#                                                #
#  Class Based  Views                            #
#                                                #
##################################################
from snippets.models import Snippets
from snippets.serializers2 import SnippetsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SnippetListView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        """
        return all objects for a get request
        """
        snippet = Snippets.objects.all()
        serializer = SnippetsSerializer(snippet, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, format=None):
        """
        create and return a jsonified/ serialized object
        """
        snipp = SnippetsSerializer(data=request.data)
        if snipp.is_valid():
            snipp.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(snipp.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SnippetDetailView(APIView):
    """
    Performing the get, put or delete an object based on certain issues
    """
    def get_detail(self, pk, format=None):
        """return an object based on its id"""
        try:
            return Snippets.objects.all()
        except Snippets.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, pk):
        """get it"""
        obj = self.get_detail(pk)
        snipp = SnippetsSerializer(obj)
        return Response(snipp.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        """update it"""
        obj = self.get_detail(pk)
        snipp = SnippetsSerializer(obj, data=request.data)
        if snipp.is_valid():
            snipp.save()
            return Response(snipp.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """delete an object based on its api"""
        obj = self.get_detail(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

####################################################
#                                                  #
# Function Based views                             #
# from rest_framework.decorators import api_view   #
#                                                  #
####################################################
#@api_view(['GET', 'POST']) 
#def snippet_list(request, format=None):
#    """
#    List of all code snippets, or create a new snippet
#    """
#    if request.method == 'GET': # get request method
#        snippets = Snippets.objects.all() # query from database/storage engine
#        serializer = SnippetsSerializer(snippets, many=True) # serializing data from storage to be jsonified
#        return Response(serializer.data) # returning a json response of the serialized data
    
#    if request.method == 'POST': # post request method
#       serializer = SnippetsSerializer(data=request.data) # serializing the post data before storing it
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED) # return serialized data from a successful post request
#        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST) # otherwise there is an error


#@api_view(['GET', 'PUT', 'DELETE'])
#def snippet_detail(request, pk, format=None): # these arguments will be passed from the url jargon
#    """
#    Retrieve, update or delete a code snippet.
#    """
#    try:
#        snippet = Snippets.objects.get(pk=pk) # always make sure that the data is valid
#    except Snippets.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND) # same as `HttpResponse(status=404)`, Response returns the correct content from an unrendered negotiation .
    
#    if request.method == 'GET':
#        serializer = SnippetsSerializer(snippet)
#        return Response(serializer.data)
    
#    if request.method == 'PUT':
#        serializer = SnippetsSerializer(snippet, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#    if request.method =='DELETE':
#        snippet.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)