from rest_framework import serializers
from apps.dictionary.models import Word

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('id', 'word', 'lang', 'main_class', 'sub_class', 'user')
