# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Invoice(models.Model):

    #__Invoice_FIELDS__
    due_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    client = models.CharField(max_length=255, null=True, blank=True)

    #__Invoice_FIELDS__END

    class Meta:
        verbose_name        = _("Invoice")
        verbose_name_plural = _("Invoice")


class Invoiceitem(models.Model):

    #__Invoiceitem_FIELDS__
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=True, blank=True)
    unit_price = models.IntegerField(null=True, blank=True)

    #__Invoiceitem_FIELDS__END

    class Meta:
        verbose_name        = _("Invoiceitem")
        verbose_name_plural = _("Invoiceitem")



#__MODELS__END
