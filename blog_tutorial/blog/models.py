'''
mauto 	models.AutoField()
mbigint 	models.BigIntegerField()
mbool 	models.BooleanField()
mchar 	models.CharField()
mcoseint 	models.CommaSeparatedIntegerField()
mdate 	models.DateField()
mdatetime 	models.DateTimeField()
mdecimal 	models.DecimalField()
memail 	models.EmailField()
mfile 	models.FileField()
mfilepath 	models.FilePathField()
mfloat 	models.FloatField()
mimg 	models.ImageField()
mint 	models.IntegerField()
mip 	models.IPAddressField()
mnullbool 	models.NullBooleanField()
mphone 	models.PhoneNumberField()
mposint 	models.PositiveIntegerField()
mpossmallin 	models.PositiveSmallIntegerField()
mslug 	models.SlugField()
msmallint 	models.SmallIntegerFiled()
mtext 	models.TextField()
mtime 	models.TimeField()
murl 	models.URLField()
musstate 	models.USStateField()
mxml 	models.XMLField()
fk 	models.ForeignKey()
m2m 	models.ManyToManyField()
o2o 	models.OneToOneField()
'''

from django.conf import settings
from django.db import models
from django.utils import timezone
'''
class creates objects, name should always start with capital letter,
models.Model param tells django this is a model
'''
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return  self.title
