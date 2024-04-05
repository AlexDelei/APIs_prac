"""
Wire the views up into these urls
"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns # adding optional format suffixes
# from rest_framework.urlpatterns -> Using format suffixes gives us URLs that explicitly refer to a given format
from snippets import views


urlpatterns = [
    path('snippets/', views.SnippetListView),
    path('snippets/<int:pk>/', views.SnippetDetailView)
]

urlpatterns = format_suffix_patterns(urlpatterns) # appending format suffixes to the existing urls