from rest_framework.generics import ListAPIView

from approvals.models import Approval
# from .serializers import ApprovalSerializer

from django.db.models import Q

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
)

from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView, 
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,)

from .pagination import ApprovalLimitOffSetPagination , ApprovalPageNumberPagination

from .permissions import IsOwnerOrReadOnly

from .serializers import (
    ApprovalListSerializer,
    ApprovalDetailSerializer, 
    ApprovalCreateUpdateSerializer,
    )

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

# class ApprovalListAPIView(ListAPIView):
#     queryset = store.objects.all()
#     serializer_class = storeSerializer

#Creating an Ambulance
class ApprovalCreateAPIView(CreateAPIView):
    queryset = Approval.objects.all()
    serializer_class = ApprovalCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class ApprovalUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Approval.objects.all()
    serializer_class = ApprovalCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class ApprovalDeleteAPIView(DestroyAPIView):
    queryset = Approval.objects.all()
    serializer_class = ApprovalDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class ApprovalDetailAPIView(RetrieveAPIView):
    queryset = Approval.objects.all()
    serializer_class = ApprovalDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class ApprovalListAPIView(ListAPIView):
    serializer_class = ApprovalListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['status']
    pagination_class = ApprovalPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Approval.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(user=id)
            print("hey you", queryset)
        return queryset
