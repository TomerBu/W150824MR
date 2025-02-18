from rest_framework import serializers

# serializers convert objects to json and vice versa
from .models import Student
from django.core.validators import MinLengthValidator, RegexValidator

from api.models import Kitten
class KittenSerializer(serializers.ModelSerializer):
    # inner class:
    class Meta:
        model = Kitten
        # fields = '__all__'
        fields = ['id', 'name', 'breed']
        # exclude = ['id']

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(2),
            RegexValidator(
                regex='^[a-zA-Z0-9]+$',
                message='name must be alphanumeric',
                code='invalid_name'
            )
        ],
        error_messages={
            'required': 'Please provide a name for the student'
        }
    )
    id = serializers.IntegerField(read_only=True)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
