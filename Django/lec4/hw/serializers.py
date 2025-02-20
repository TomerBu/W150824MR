from rest_framework.serializers import ModelSerializer
from .models import FunFact

class FunFactsSerializer(ModelSerializer):
    class Meta:
        model = FunFact
        # fields = ['id', 'fact', 'source']
        fields = '__all__'
        # exclude = ['password']