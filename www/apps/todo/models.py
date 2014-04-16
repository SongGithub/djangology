from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse


PRIORITY_CHOICES = (
    (0, 'Low'),
    (1, 'Normal'),
    (2, 'High'),
)

# COMPLETESTATUS
class Category(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=250)

    # #Self Naming Function_for 'Slug'
    def save(self, *args, **kwargs):
        # turns "Some Category Name" into "some-category-name"
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-update-delete', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Categories'


class Item(models.Model):
    category = models.ForeignKey(Category)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    create_date = models.DateTimeField('date created',auto_now_add=True)
    due_date = models.DateTimeField('date due', null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=0)
    status = models.BooleanField(
         default=False
      )


    class Meta:
        verbose_name_plural = 'Items'

    # #Self Naming Function_for 'Slug'
    def save(self, *args, **kwargs):
        # turns "Some Category Name" into "some-category-name"
        self.slug = slugify(self.name)
        return super(Item, self).save(*args, **kwargs)

        def __unicode__(self):
            return self.name
