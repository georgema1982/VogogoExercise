from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

# Create your models here.
class Item(models.Model):

    name = models.CharField(max_length = 50)
    code = models.CharField(max_length = 50, unique = True, validators = [RegexValidator(r'^\d*$', 'Code should be made of digits.')])

    def __unicode__(self):
        return self.name

class Price(models.Model):

    item = models.ForeignKey(Item)
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField(default = True)

    class Meta(object):
        ordering = ('-quantity',)
        unique_together = ('item', 'quantity')

    def __unicode__(self):
        return self.quantity == 1 and _('$%(price).2f ea') % {'price': self.price} or _('%(quantity)d/$%(price).2f') % {'quantity': self.quantity, 'price':self.price}
