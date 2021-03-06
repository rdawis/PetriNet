from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import uuid
# Create your models here.

class Unit(MPTTModel):
    uuid_name = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    human_readable_name = models.CharField(
        max_length=50,
        unique=True
    )

    form = 'O'
    transform = 'L'
    shape_choices = (
        (form, 'Form'),
        (transform,'Transform')
    )
    shape = models.CharField(
        max_length=1,
        choices=shape_choices
    )

    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        db_index=True
    )

    # x_val = models.DecimalField(max_digits=13, decimal_places=9, default=0)
    # y_val = models.DecimalField(max_digits=13, decimal_places=9, default=0)
    x_val = models.FloatField(default=0)
    y_val = models.FloatField(default=0)
    class MPTTMeta:
        order_insertion_by = ['human_readable_name']
    def __unicode__(self):
        return self.human_readable_name
class Connection(models.Model):
    source = models.ForeignKey(Unit,related_name='dest')
    destination = models.ForeignKey(Unit,related_name='src')
    def __unicode__(self):
        return '%s to %s' % (self.source, self.destination)
