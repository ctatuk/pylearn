from django.urls import path
from django import view

urlpatterns = [
    path('', view.index),
    path('contacts', view.contacts),
    path('status', view.status),
    path('publish', view.publish),
    path('publications/<int:number>', view.publication),
    path('publications/<int:number>', view.publication),
