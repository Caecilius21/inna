from apps.dictionary.models import *
from apps.dictionary.serializers import WordSerializer
from rest_framework import generics


class WordListCreate(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
