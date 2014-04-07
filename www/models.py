from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
import datetime

PRIORITY_CHOICES = (
    (0, 'Low'),
    (1, 'Normal'),
    (2, 'High'),
)

COMPLETESTATUS_CHOICES = (
    (False, 'Not Yet'),
    (True, 'Completed')
)

class Category(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=20)
    description = models. CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'Categories'


    # #Self Naming Function_for 'Slug'
    def save(self, *args, **kwargs):
        # turns "Some Category Name" into "some-category-name"
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category)
    slug = models.SlugField(unique=True)
    itemname = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    create_date = models.DateTimeField('date created', null=True, blank=True)
    due_date = models.DateTimeField('date due', null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=0)
    completeStatus = models.BooleanField(
        choices=COMPLETESTATUS_CHOICES,
        default=False
      )

    class Meta:
        verbose_name_plural = 'Items'

    # #Self Naming Function_for 'Slug'
    def save(self, *args, **kwargs):
        # turns "Some Category Name" into "some-category-name"
        self.slug = slugify(self.itemname)
        super(Item, self).save(*args, **kwargs)
        ''' On save, update timestamps '''
        self.create_date = datetime.datetime.today()
        # self.Due_date = datetime.datetime.today()
        return super(Item, self).save(*args, **kwargs)

        def __unicode__(self):
            return self.itemname
