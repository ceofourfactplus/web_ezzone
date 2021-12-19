from django.db.models import fields
from rest_framework import serializers

from backend.promotion.models import PointPromotion

class PointSerializer(serializers.Model):
  class Meta:
    models = PointPromotion
    fields = []
