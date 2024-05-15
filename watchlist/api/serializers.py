from rest_framework import serializers

from watchlist.models import Product, Platform, Review


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

class ReviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # fields = '__all__'
        fields = ('id', 'rating', 'description', 'is_active', 'product')


class ProductModelSerializer(serializers.ModelSerializer):
    reviews = ReviewModelSerializer(many=True, read_only=True)

    # reviews = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('id', 'title', 'description', 'is_active', 'platform', 'reviews',)


class PlatformModelSerializer(serializers.ModelSerializer):
    products = ProductModelSerializer(many=True, read_only=True)

    # products = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='product-detail')
    # products = serializers.StringRelatedField(many=True)

    class Meta:
        model = Platform
        # fields = '__all__'
        fields = ('id', 'name', 'about', 'website', 'products')
