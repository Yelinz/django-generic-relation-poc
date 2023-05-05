from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Person(models.Model):
    name = models.CharField(max_length=200)
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, null=True, blank=True
    )
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey("content_type", "object_id")


class Team(models.Model):
    team_name = models.CharField(max_length=200)
    persons = GenericRelation(
        Person,
        related_query_name="team",
        content_type_field="content_type",
        object_id_field="object_id",
    )


class Location(models.Model):
    location_name = models.CharField(max_length=200)
    persons = GenericRelation(
        Person,
        related_query_name="location",
        content_type_field="content_type",
        object_id_field="object_id",
    )
