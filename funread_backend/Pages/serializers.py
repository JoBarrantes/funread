from unicodedata import name
from rest_framework import serializers

from Books.serializers import BookSerializer
from .models import Pages
from Pages.templates import Template
class PageSerializer(serializers.ModelSerializer):

  class Meta:
    model = Pages
    fields = '__all__'

  def create(self, validated_data):
      return Pages.objects.create(**validated_data)

  def update(self, instance, validated_data):
      instance.pageid = validated_data.get('pageid', instance.pageid)
      instance.bookid = validated_data.get('bookid', instance.bookid)
      instance.elementorder = validated_data.get('elementorder', instance.elementorder)
      instance.type = validated_data.get('type', instance.type)
      instance.template = validated_data.get('template', instance.template)
      instance.gridDirection = validated_data.get('gridDirection', instance.gridDirection)
      instance.gridNumRows = validated_data.get('gridNumRows', instance.gridNumRows)
      instance.save()
      return instance


class getTemplate():
  def gettemplate(self, templateerquest):
    template_json = Template.getTemplate(templateerquest)
    return template_json
  