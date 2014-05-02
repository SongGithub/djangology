from django.conf.urls import patterns
# from django.conf.urls import include
from django.conf.urls import url
from www.apps.todo import views
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(
        r'^categories$', 
        views.CategoryListView.as_view(),
        name='category-list'
    ),  
    url(
        r'^categories/(?P<slug>[\w-]+)$', 
        views.CategoryUpdateDeleteView.as_view(),
        name='category-update-delete'
    ), 

    url(
        r'^categories/(?P<slug>[\w-]+)/items$', 
        views.CategoryItemListView.as_view(), name='category-item-list'
    ),

    url(
        r'^categories/(?P<cat_slug>[\w-]+)/items/(?P<slug>[\w-]+)$', 
        views.CategoryItemUpdateDeleteView.as_view(), 
        name='category-item-update-delete'
    ), 
)