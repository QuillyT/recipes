from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    def _str_(self):
        return self.name
