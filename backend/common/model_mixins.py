from django.db import models


class CreatedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        abstract = True
        get_latest_by = 'created'


class ModifiedMixin(models.Model):
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if 'update_fields' in kwargs and 'modified' not in kwargs['update_fields']:
            kwargs['update_fields'] = ['modified', *kwargs['update_fields']]

        return super().save(*args, **kwargs)

    def direct_save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True


class CreatedModifiedMixin(CreatedMixin, ModifiedMixin):
    class Meta(CreatedMixin.Meta):
        abstract = True
