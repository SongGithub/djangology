#this file is equal to 'Form.py'
from rest_framework import serializers
from . import models

class ItemSerializer(serializers.ModelSerializer):
    """
    Serializer to parse Item data
    """
    class Meta:
        model = models.Item
        field = (
            'category',
            'slug',
            'name',
            'description',
            'create_date',
            'due_data',
            'priority',
            'status',
        )


class CategorySerializer(serializers.ModelSerializer):   
    """
    Serializer to parse Category data
    """

    link = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = models.Category
        fields = (
            'slug',
            'name',
            'description',
            'link'
        )
  