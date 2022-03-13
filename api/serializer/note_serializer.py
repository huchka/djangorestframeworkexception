import logging

from api.models import Note
from rest_framework import serializers


# logging
logger = logging.getLogger(__file__)


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        exclude = ['modified_datetime']
