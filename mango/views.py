from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, viewsets, permissions
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from rest_framework_simplejwt.authentication import JWTAuthentication

from mango.models import Card, Review
from mango.serializers import CardSerializer, ReviewSerializer, CardDetailSerializer, ReviewCreateSerializer


class ReviewPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class CardPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 12


class ReviewListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = ReviewPagination
    authentication_classes = [JWTAuthentication]


class ReviewCreateAPIView(CreateAPIView):
    serializer_class = ReviewCreateSerializer
    permission_classes = (IsAuthenticated, )

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        review = Review.objects.create(
            text=serializer.validated_data["text"],
            mango_id=serializer.validated_data["mango_id"],
            user_id=request.user.id
        )
        review.save()
        return Response(data=ReviewSerializer(review).data)


# class ReviewViewSet(CreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewCreateSerializer
#     # permission_classes = [IsAuthenticatedOrReadOnly]
#     # authentication_classes = [JWTAuthentication]


class CardAPIView(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'year']
    pagination_class = CardPagination



class CardDetailAPIView(APIView):

    def get(self, request, id):
        try:
            queryset = Card.objects.get(id=id)
        except:
            return Response(data={'errors': 'Card not found'}, status=404)
        serializer = CardDetailSerializer(queryset)
        return Response({
            "card": serializer.data
        })