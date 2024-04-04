"""
writing regular django views using our serializer

Implementing some API views using our new Serializer class
"""
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippets
from snippets.serializers2 import SnippetsSerializer


@csrf_exempt
def snippet_list(request):
    """
    List of all code snippets, or create a new snippet
    """
    if request.method == 'GET':
        snippets = Snippets.objects.all()
        serializer = SnippetsSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippets.objects.get(pk=pk)
    except Snippets.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = SnippetsSerializer(snippet)
        return JsonResponse(serializer.data)
    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetsSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    if request.method =='DELETE':
        snippet.delete()
        return HttpResponse(status=204)