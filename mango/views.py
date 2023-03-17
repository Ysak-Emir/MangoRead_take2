from rest_framework import generics, filters, status
from rest_framework.generics import CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from mango.models import MangoCard, Review
from mango.serializers import CardListSerializer, ReviewSerializer, CardDetailSerializer, ReviewCreateSerializer, CardCreateSerializer

# --- PAGINATION ---

class ReviewPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class CardPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 12

# --- CARD ---

class MangoCardCreateAPIView(APIView):
    def post(self, request, format=None):
        serializer = CardCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"Отзыв создан": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(data={"Что-то пошло не так!": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class MangoCardListAPIView(generics.ListAPIView):
    queryset = MangoCard.objects.all()
    serializer_class = CardListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'year']
    pagination_class = CardPagination

class MangoCardDetailAPIView(APIView):

    def get(self, request, id):
        try:
            queryset = MangoCard.objects.get(id=id)
        except:
            return Response(data={'errors': 'Card not found'}, status=404)
        serializer = CardDetailSerializer(queryset)
        return Response({
            "card": serializer.data
        })

# --- REVIEW ---

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






