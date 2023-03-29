from datetime import timezone
from django.db import models


class Audit(models.Model):
    created_on = models.DateTimeField(auto_now=True)
    modified_on = models.DateTimeField(auto_now=True)
    deleted_on = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        # Esto significa, que solo quiero su comportamiento y no un modelo con el nombre Audit.
        abstract = True

    def safe_delete(self):
        self.is_active = False
        self.deleted_on = timezone.now()
        self.save()


class WithoutDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
