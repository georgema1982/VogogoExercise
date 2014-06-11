from django.forms.models import BaseInlineFormSet
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class PriceInlineFormSet(BaseInlineFormSet):

    def clean(self):
        super(PriceInlineFormSet, self).clean()
        base_price = False
        for form in self.forms:
            instance = form.instance
            if instance.quantity == 1 and instance.active:
                base_price = True
                break
        if not base_price: raise ValidationError(_("Can't find an active base price. A base price is a price for quantity one."))