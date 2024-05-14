from rest_framework.response import Response
from rest_framework.views import APIView

from watchlist.api.serializers import ProductModelSerializer, PlatformModelSerializer
from watchlist.models import Product, Platform


class ProductsView(APIView):
    products = Product.objects.all()

    def get(self, request):
        serializer = ProductModelSerializer(self.products, many=True)
        return Response(serializer.data, 200, )

    def post(self, request):
        serializer = ProductModelSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, 400, )

        serializer.save()
        return Response(serializer.data, 201, )


class ProductDetailView(APIView):
    products = Product.objects.all()

    def get(self, request, product_id):
        serializer = ProductModelSerializer(self.products.get(pk=product_id))
        return Response(serializer.data, 200, )

    def put(self, request, product_id):
        product = self.products.get(pk=product_id)
        serializer = ProductModelSerializer(product, data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, 400, )

        serializer.save()
        return Response(serializer.data, 201, )

    def delete(self, request, product_id):
        product = self.products.get(pk=product_id)
        product.delete()
        return Response(status=204)


class PlatformsView(APIView):
    platform = Platform.objects.all()

    def get(self, request):
        serializer = PlatformModelSerializer(self.platform, many=True, )
        # serializer = PlatformModelSerializer(self.platform, many=True, context={'request': request})
        return Response(serializer.data, 200, )

    def post(self, request):
        serializer = PlatformModelSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, 400, )

        serializer.save()
        return Response(serializer.data, 201, )


class PlatformDetailView(APIView):
    platform = Platform.objects.all()

    def get(self, request, platform_id):
        serializer = PlatformModelSerializer(self.platform.get(pk=platform_id))
        return Response(serializer.data, 200, )

    def put(self, request, platform_id):
        plaform = self.platform.get(pk=platform_id)
        serializer = PlatformModelSerializer(plaform, data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, 400, )

        serializer.save()
        return Response(serializer.data, 201, )

    def delete(self, request, platform_id):
        plaform = self.platform.get(pk=platform_id)
        plaform.delete()
        return Response(status=204)
