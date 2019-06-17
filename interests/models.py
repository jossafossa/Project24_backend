from django.db import models

class Interest(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
    def ___str___(self):
        return self.name

