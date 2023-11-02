from rest_framework import serializers
from . models import Discount


class DiscountSerializer(serializers.Serializer):

    title = serializers.CharField(max_length=100,  null=True, blank=True)
    img = serializers.ImageField()
    description = serializers.TextField()
    start_data = serializers.DateTimeField()
    ending_data = serializers.DateTimeField()
    price = serializers.DecimalField(max_digits=10, decimal_places=3)


class Meta:
    model = Discount
    fields = ['id', 'title', 'image', 'description', 'start_data', 'ending_data', 'price']

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('description', instance.description)
        instance.start_data = validated_data.get('start_data', instance.start_data)
        instance.ending_data = validated_data.get('ending_data', instance.ending_data)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
