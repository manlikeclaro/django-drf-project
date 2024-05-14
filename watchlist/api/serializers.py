from rest_framework import serializers

from watchlist.models import Product, Platform


# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     description = serializers.CharField()
#     is_active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         product = Product.objects.create(**validated_data)
#         return product
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.is_active = validated_data.get('is_active', instance.is_active)
#         instance.save()
#         return instance


class ProductModelSerializer(serializers.ModelSerializer):
    len_title = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('name', 'description', 'is_active', )
        # exclude = ('id', )

    def get_len_title(self, object):
        result = len(object.title)
        return result


class PlatformModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'
