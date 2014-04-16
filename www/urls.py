from django.conf.urls import patterns, include, url
from django.contrib import admin
from www.apps.todo import views
admin.autodiscover()
#IMPORTANT:
#Being restful, there should be NO VERB in URL at all, shall be NOUN which 
#represent resource.
urlpatterns = patterns('',
    ##################################################################
    url(r'^$', views.IndexView.as_view(), name='home'),
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

    url(r'^admin/', include(admin.site.urls)),
)


# 'URL layout design guide'
# /<category_slug>/
# /<category_slug>/add/
# /<category_slug>/delete/
# /<category_slug>/edit/
# /<category_slug>/items/<item_slug>/
# /<category_slug>/<item_slug>/add/
# /<category_slug>/<item_slug>/delete/
# /<category_slug>/<item_slug>/edit/

# REST API
# --------

# GET A LIST OF categories

#   GET /categories/

# CREATE NEW
#   POST /categories/ 

# Fetch selected items:

#   GET /categories/<slug>/

# Delete

#   DELETE /categories/<slug>/

# UPDATE

#   PUT /categories/<slug>/

# /categories/<slug>/items

# /categories/<slug>/item/<slug>