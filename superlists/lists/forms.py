from django import forms
from .models import Item
from django.utils.translation import gettext as _

EMPTY_ITEM_ERROR = _("You can't have an empty list item")

class ItemForm(forms.ModelForm):
    def save(self, for_list=None, commit=True):
        self.instance.list = for_list
        return super().save(commit=commit)

    class Meta:
        model = Item
        fields = ('text', )
        widgets = {
            'text': forms.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
                'class': 'form-control input-lg'
            })
        }
        error_messages = {
            'text': {'required': EMPTY_ITEM_ERROR}
        }