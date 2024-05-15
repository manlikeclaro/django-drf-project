from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

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


class ProductReviewsView(ListCreateAPIView):
    serializer_class = ReviewModelSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        queryset = Review.objects.filter(product=product_id)
        return queryset


class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer
