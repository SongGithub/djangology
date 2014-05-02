from django.shortcuts import get_object_or_404
from django.views import generic
from rest_framework import generics

from . import models
from . import serializers


class CategoryListView(generics.ListCreateAPIView):
    serializer_class = serializers.CategorySerializer
    model = models.Category

class CategoryUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CategorySerializer
    model = models.Category


class CategoryMixin(object):

    category_slug = 'slug'

    def get_category(self):
        slug = self.kwargs.get(self.category_slug)
        return get_object_or_404(models.Category, slug=slug)


class CategoryItemListView(CategoryMixin, generics.ListCreateAPIView):
    serializer_class = serializers.ItemSerializer
    model = models.Item
    # filter_fields = ('status',)

    def get_queryset(self):
        qs = super(CategoryItemListView, self).get_queryset()
        return qs.filter(category=self.get_category())


class CategoryItemUpdateDeleteView(
    CategoryMixin,
    generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = serializers.ItemSerializer
    model = models.Item
    category_slug = 'cat_slug'

    def get_queryset(self):
        qs = super(CategoryItemUpdateDeleteView, self).get_queryset()
        return qs.filter(category=self.get_category())


class Home(generic.TemplateView):
    template_name = 'index.html'