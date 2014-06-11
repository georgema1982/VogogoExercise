from django.contrib import admin
from checkout.models import Price, Item
from django.forms.models import inlineformset_factory
from checkout.forms import PriceInlineFormSet

class PriceAdmin(admin.TabularInline):
    model = Price
    formset = inlineformset_factory(Item, Price, formset = PriceInlineFormSet)

class ItemAdmin(admin.ModelAdmin):
    inlines = (PriceAdmin,)

# Register your models here.
admin.site.register(Item, ItemAdmin)
