from __future__ import unicode_literals

from django.db import models

class Box(models.Model):
    box_name = models.CharField(max_length=255)
    box_author = models.CharField(max_length=255)
    box_url = models.CharField(max_length=2500)
    box_os = models.CharField(max_length=250)
    box_checksum = models.CharField(max_length=512)
    # TODO: need to create a separate table for builders and add laterwards
    box_builders = models.CharField(max_length=100)

    def __str__(self):
        return self.box_name



