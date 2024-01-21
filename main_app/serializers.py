from rest_framework import serializers
from . import models
from .models import DATA22


class UploadFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Upload_File
        fields = '__all__'


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mark
        fields = '__all__'


class Mark22Serializer(serializers.ModelSerializer):
    count_of_unique_models = serializers.IntegerField()

    class Meta:
        model = models.Mark
        fields = ['mark_name', 'count_of_unique_models']


class Mark21Serializer(serializers.ModelSerializer):
    count_of_unique_models = serializers.IntegerField()

    class Meta:
        model = models.Mark
        fields = ['mark_name', 'count_of_unique_models']


class ModelCountSerializer(serializers.Serializer):
    model_name = serializers.CharField()
    count_of_models = serializers.IntegerField()


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Model1
        fields = '__all__'


class UploadFile2Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Upload_File2
        fields = '__all__'


class Data21Serializer(serializers.Serializer):
    model_name = serializers.CharField(source='model__model_name')
    count_from_that_model = serializers.IntegerField()

    class Meta:
        fields = ['model_name', 'count_from_that_model']


class Data22Serializer(serializers.Serializer):
    model_name = serializers.CharField(source='model__model_name')
    count_from_that_model = serializers.IntegerField()

    class Meta:
        fields = ['model_name', 'count_from_that_model']


class MonthlyModelCountSerializer(serializers.Serializer):
    month = serializers.SerializerMethodField()
    count_of_models = serializers.IntegerField()

    def get_month(self, instance):
        return instance['month']

    def to_representation(self, instance):
        month_mapping = {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December',
        }

        numeric_month = instance['month']
        month_name = month_mapping.get(numeric_month, '')

        return {
            'month': month_name,
            'count_of_models': instance['count_of_models']
        }
