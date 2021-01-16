from oscar.apps.catalogue.abstract_models import AbstractOption
from django.db import models
from django.utils.translation import gettext_lazy as _
from oscar.apps.catalogue.models import *
from oscar.models.fields import AutoSlugField, NullCharField
from oscar.core.decorators import deprecated

class AbstractOption(AbstractOption):
    """
        An option that can be selected for a particular item when the product
        is added to the basket.
        For example,  a list ID for an SMS message send, or a personalised message
        to print on a T-shirt.
        This is not the same as an 'attribute' as options do not have a fixed value
        for a particular item.  Instead, option need to be specified by a customer
        when they add the item to their basket.
        The `type` of the option determines the form input that will be used to
        collect the information from the customer, and the `required` attribute
        determines whether a value must be supplied in order to add the item to the basket.
        """

    # Option types
    TEXT = "text"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    DATE = "date"

    TYPE_CHOICES = (
        (TEXT, _("Text")),
        (INTEGER, _("Integer")),
        (BOOLEAN, _("True / False")),
        (FLOAT, _("Float")),
        (DATE, _("Date")),
    )

    name = models.CharField(_("Name"), max_length=128, db_index=True)
    code = AutoSlugField(_("Code"), max_length=128, unique=True, populate_from='name')
    type = models.CharField(_("Type"), max_length=255, default=TEXT, choices=TYPE_CHOICES)
    required = models.BooleanField(_("Is this option required?"), default=False)

    class Meta:
        abstract = True
        app_label = 'catalogue'
        ordering = ['name']
        verbose_name = _("Option")
        verbose_name_plural = _("Options")

    def __str__(self):
        return self.name

    @property
    @deprecated
    def is_required(self):
        return self.required

