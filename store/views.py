from django.http.response import HttpResponse
from urllib import request
from store.serializers import ProductSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Product
from .tasks import *
from rest_framework import status, generics
from django.conf import settings
from rest_framework.response import Response
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


def home(request):
    return HttpResponse("Hello World")


def total(request):
    res = add.delay(4, 5)
    return HttpResponse(res)


from django.core.cache import cache

cache.set("foo", "bar")


class ProductView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

    def create(self, request, *args, **kwargs):
        product_serializer = self.get_serializer(data=self.request.data)

        if not product_serializer.is_valid():
            return Response(
                {"message": "Created Product unsuccessfully!", "success": False},
                status=status.HTTP_400_BAD_REQUEST,
            )

        product_serializer.save()

        return Response(
            data={"message": "Created Product successfully!", "success": True},
            status=status.HTTP_201_CREATED,
        )

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        product_pk = self.kwargs.get("pk")
        existing_product = get_object_or_404(self.queryset, id=product_pk)

        product_serializer = self.serializer_class(
            existing_product
        )
        return Response(product_serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        product_pk = self.kwargs.get("pk")
        existing_product = get_object_or_404(self.queryset, id=product_pk)

        product_info_dict = self.request.data
        product_serializer = self.serializer_class(
            existing_product, data=product_info_dict, partial=True
        )

        if not product_serializer.is_valid():
            return Response(
                {"message": "Updated product unsuccessfully!", "success": False},
                status=status.HTTP_400_BAD_REQUEST,
            )

        product_serializer.save()

        return Response(
            data={"message": "Updated product successfully!", "success": True},
            status=status.HTTP_200_OK,
        )

    def destroy(self, request, *args, **kwargs):
        product_pk = self.kwargs.get("pk")
        existing_product = get_object_or_404(self.queryset, id=product_pk)

        existing_product.delete()

        return Response(
            data={"message": "Deleted Product successfully!", "success": True},
            status=status.HTTP_200_OK,
        )


@api_view(["GET"])
def view_cached_products(request):
    if "product" in cache:
        # get results from cache
        products = cache.get("product")
        return Response(products, status=status.HTTP_201_CREATED)
    else:
        products = Product.objects.all()
        results = [product.to_json() for product in products]
        # store data in cache
        cache.set("product", results, timeout=CACHE_TTL)
        return Response(results, status=status.HTTP_201_CREATED)
