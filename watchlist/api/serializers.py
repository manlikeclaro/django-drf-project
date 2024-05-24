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
    author = serializers.StringRelatedField(read_only=True)
    movie = serializers.StringRelatedField(source='product', read_only=True)

    class Meta:
        model = Review
        # fields = '__all__'
        fields = ('id', 'author', 'rating', 'movie', 'description', 'is_active',)


class ProductModelSerializer(serializers.ModelSerializer):
    streaming_platform = serializers.StringRelatedField(source='platform', read_only=True)

    # reviews = ReviewModelSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        # fields = '__all__'
        fields = (
            'id', 'title', 'description', 'streaming_platform', 'average_rating', 'total_reviews',
            'is_active', 'platform'
        )


class PlatformModelSerializer(serializers.ModelSerializer):
    # movies = ProductModelSerializer(many=True, read_only=True)
    # movies = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='product-detail')
    # movies = serializers.StringRelatedField(many=True)

    class Meta:
        model = Platform
        # fields = '__all__'
        fields = ('id', 'name', 'about', 'website', 'total_movies',)
