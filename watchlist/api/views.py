from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from watchlist.api.permissions import AdminOrReadOnly, ReviewAuthorOrReadOnly
from watchlist.api.serializers import ProductModelSerializer, PlatformModelSerializer, ReviewModelSerializer
from watchlist.models import Product, Platform, Review


class ProductsView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


# class ProductsView(APIView):
#     products = Product.objects.all()
#
#     def get(self, request):
#         serializer = ProductModelSerializer(self.products, many=True)
#         # serializer = ProductModelSerializer(self.products, many=True, context={'request': request})
#         return Response(serializer.data, 200, )
#
#     def post(self, request):
#         serializer = ProductModelSerializer(data=request.data)
#
#         if not serializer.is_valid():
#             return Response(serializer.errors, 400, )
#
#         serializer.save()
#         return Response(serializer.data, 201, )


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = [AdminOrReadOnly]


# class ProductDetailView(APIView):
#     products = Product.objects.all()
#
#     def get(self, request, product_id):
#         serializer = ProductModelSerializer(self.products.get(pk=product_id))
#         # serializer = ProductModelSerializer(self.products.get(pk=product_id), context={'request': request})
#         return Response(serializer.data, 200, )
#
#     def put(self, request, product_id):
#         product = self.products.get(pk=product_id)
#         serializer = ProductModelSerializer(product, data=request.data)
#
#         if not serializer.is_valid():
#             return Response(serializer.errors, 400, )
#
#         serializer.save()
#         return Response(serializer.data, 201, )
#
#     def delete(self, request, product_id):
#         product = self.products.get(pk=product_id)
#         product.delete()
#         return Response(status=204)


class PlatformsView(ListCreateAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformModelSerializer


# class PlatformsView(APIView):
#     platform = Platform.objects.all()
#
#     def get(self, request):
#         serializer = PlatformModelSerializer(self.platform, many=True, )
#         # serializer = PlatformModelSerializer(self.platform, many=True, context={'request': request})
#         return Response(serializer.data, 200, )
#
#     def post(self, request):
#         serializer = PlatformModelSerializer(data=request.data)
#
#         if not serializer.is_valid():
#             return Response(serializer.errors, 400, )
#
#         serializer.save()
#         return Response(serializer.data, 201, )


class PlatformDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformModelSerializer
    permission_classes = [AdminOrReadOnly]


# class PlatformDetailView(APIView):
#     platform = Platform.objects.all()
#
#     def get(self, request, platform_id):
#         serializer = PlatformModelSerializer(self.platform.get(pk=platform_id))
#         # serializer = PlatformModelSerializer(self.platform.get(pk=platform_id), context={'request': request})
#         return Response(serializer.data, 200, )
#
#     def put(self, request, platform_id):
#         plaform = self.platform.get(pk=platform_id)
#         serializer = PlatformModelSerializer(plaform, data=request.data)
#
#         if not serializer.is_valid():
#             return Response(serializer.errors, 400, )
#
#         serializer.save()
#         return Response(serializer.data, 201, )
#
#     def delete(self, request, platform_id):
#         plaform = self.platform.get(pk=platform_id)
#         plaform.delete()
#         return Response(status=204)


class ProductReviewsView(ListAPIView):
    serializer_class = ReviewModelSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        queryset = Review.objects.filter(product=product_id)
        return queryset


class CreateProductReviewView(CreateAPIView):
    serializer_class = ReviewModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Review.objects.all()
        return queryset

    def perform_create(self, serializer):
        product_id = self.kwargs['product_id']
        movie = Product.objects.get(pk=product_id)

        reviewer = self.request.user
        review_made = Review.objects.filter(author=reviewer, product=movie)

        if review_made.exists():
            raise ValidationError('You have already reviewed this product')

        # movie.total_reviews += movie.total_reviews
        # movie.average_rating = (movie.average_rating + serializer.validated_data['rating']) / movie.total_reviews
        # movie.save()

        serializer.save(product=movie, author=reviewer)


class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer
    permission_classes = [ReviewAuthorOrReadOnly]


class APIRootView(APIView):
    def get(self, request, format=None):
        paths = {
            'platforms': reverse('platforms-list', request=request, format=format),
            'platform detail': reverse('platform-detail', kwargs={'pk': 1}, request=request, format=format),
            'products': reverse('products-list', request=request, format=format),
            'product detail': reverse('product-detail', kwargs={'pk': 1}, request=request, format=format),
            'product reviews': reverse('product-reviews', kwargs={'product_id': 1}, request=request, format=format),
            'create review': reverse('create-review', kwargs={'product_id': 1}, request=request, format=format),
            'review detail': reverse('review-detail', kwargs={'pk': 1}, request=request, format=format),

        }
        return Response(paths)
