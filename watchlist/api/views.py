from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.views import APIView

from watchlist.api.pagination import CustomPageNumberPagination
from watchlist.api.permissions import IsAdminOrReadOnly, IsReviewAuthorOrReadOnly
from watchlist.api.serializers import ProductModelSerializer, PlatformModelSerializer, ReviewModelSerializer
from watchlist.api.throttling import FormattedUserRateThrottle, FormattedAnonRateThrottle
from watchlist.models import Product, Platform, Review


class PlatformsView(ListCreateAPIView):
    # queryset = Platform.objects.all()
    queryset = Platform.objects.exclude(is_active=False)
    serializer_class = PlatformModelSerializer
    permission_classes = [IsAdminOrReadOnly]
    throttle_classes = [FormattedUserRateThrottle, FormattedAnonRateThrottle]
    pagination_class = CustomPageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['name']


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
    permission_classes = [IsAdminOrReadOnly]


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


class ProductsView(ListCreateAPIView):
    queryset = Product.objects.all()
    # queryset = Product.objects.exclude(is_active=False)
    serializer_class = ProductModelSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['^title', '=platform__name']
    ordering_fields = ['average_rating']


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
    permission_classes = [IsAdminOrReadOnly]


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


class ProductReviewsView(ListAPIView):
    serializer_class = ReviewModelSerializer

    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        # queryset = Review.objects.filter(product=product_id, )
        queryset = Review.objects.filter(product=product_id, ).exclude(is_active=False)
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

        serializer.save(product=movie, author=reviewer)


class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer
    permission_classes = [IsReviewAuthorOrReadOnly, IsAdminUser]


class UserReview(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['author__username']
    search_fields = ['author__username']
    pagination_class = CustomPageNumberPagination

    # def get_queryset(self):
    #     user_name = self.kwargs['user_name']
    #     queryset = Review.objects.filter(author__username=user_name)
    #     return queryset

    # def get_queryset(self):
    #     queryset = Review.objects.all()
    #     user_name = self.request.query_params.get('username', None)
    #
    #     if user_name is not None:
    #         queryset = queryset.filter(author__username=user_name)
    #     return queryset


class APIRootView(APIView):
    def get(self, request, format=None):
        paths = {
            'platforms': reverse('platforms-list', request=request, format=format),
            'platform detail': reverse('platform-detail', kwargs={'pk': 1}, request=request, format=format),
            'products': reverse('products-list', request=request, format=format),
            'product detail': reverse('product-detail', kwargs={'pk': 1}, request=request, format=format),
            'user reviews': reverse('user-reviews', request=request, format=format),
            'product reviews': reverse('product-reviews', kwargs={'product_id': 1}, request=request, format=format),
            'review detail': reverse('review-detail', kwargs={'pk': 1}, request=request, format=format),
            'create review': reverse('create-review', kwargs={'product_id': 1}, request=request, format=format),
            'documentation/swagger ui': reverse('swagger-ui', request=request, format=format),
            'documentation/redoc': reverse('redoc', request=request, format=format),

        }
        return Response(paths)
