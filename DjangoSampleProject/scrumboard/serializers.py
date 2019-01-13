"""Serializer has been created to send data to client-side framework in JSON format"""
from rest_framework import serializers
from .models import List, Card

# This serialises the data in python to JSON format

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"


class ListSerializer(serializers.ModelSerializer):
    cards = CardSerializer(read_only=True, many=True)
    class Meta:
        model = List
        fields = "__all__"
