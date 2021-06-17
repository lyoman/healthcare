from rest_framework.generics import ListAPIView

from patients.models import Patient
# from .serializers import PatientSerializer

from django.db.models import Q

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
)

from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView, 
    RetrieveAPIView,
    RetrieveUpdateAPIView,)

from .pagination import PatientLimitOffSetPagination , PatientPageNumberPagination

from .permissions import IsOwnerOrReadOnly

from .serializers import (
    PatientListSerializer,
    PatientDetailSerializer, 
    PatientCreateUpdateSerializer,
    )

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

# class PatientListAPIView(ListAPIView):
#     queryset = store.objects.all()
#     serializer_class = storeSerializer

class PatientUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientCreateUpdateSerializer
    lookup_field = 'id'
    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class PatientDeleteAPIView(DestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class PatientDetailAPIView(RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class PatientListAPIView(ListAPIView):
    serializer_class = PatientListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['patient_name', 'patient_id', 'heart_rate', 'patient_history']
    pagination_class = PatientPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Patient.objects.all()
        # queryset_list = Patient.objects.filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(patient_name__icontains=query)|
                Q(temperature__icontains=query)|
                Q(patient_id__icontains=query)
                ).distinct()
        return queryset_list
