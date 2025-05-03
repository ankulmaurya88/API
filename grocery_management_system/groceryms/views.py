from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Categories, Products, Sales, Customers, Suppliers, Purchases, Payments
from .serializers import CategorySerializer, ProductSerializer, SaleSerializer

import logging

logger = logging.getLogger('grocery')

# Categories API View
class CategoryList(APIView):
    def get(self, request):
        try:
            categories = Categories.objects.all()
            serializer = CategorySerializer(categories, many=True)
            logger.info("Fetched all categories successfully.")
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error fetching categories: {e}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.info("Created new category successfully.")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            logger.warning(f"Invalid category data: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error creating category: {e}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Product API View
class ProductList(APIView):
    def get(self, request):
        try:
            products = Products.objects.all()
            serializer = ProductSerializer(products, many=True)
            logger.info("Fetched all products successfully.")
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error fetching products: {e}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.info("Created new product successfully.")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            logger.warning(f"Invalid product data: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error creating product: {e}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Sale API View
class SaleList(APIView):
    def get(self, request):
        try:
            sales = Sales.objects.all()
            serializer = SaleSerializer(sales, many=True)
            logger.info("Fetched all sales successfully.")
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error fetching sales: {e}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = SaleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.info("Created new sale successfully.")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            logger.warning(f"Invalid sale data: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error creating sale: {e}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
