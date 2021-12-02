from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from django_filters.rest_framework.filters import DateFromToRangeFilter
from django_filters import FilterSet

from .serializers.counters import CounterSerializer
from .serializers.history import HistorySerializer
from counter.models import History


class HistoryFilter(FilterSet):
    period = DateFromToRangeFilter()

    class Meta:
        model = History
        fields = ['period']


class CounterViewSet(ModelViewSet):
    serializer_class = CounterSerializer

    def get_queryset(self):
        return self.request.user.counters.all()

    @action(detail=True, methods=['get'], serializer_class=HistorySerializer)
    def history(self, request, pk=None):
        queryset = History.objects.filter(
            counter=self.get_object()
        ).order_by('-period')
        filtered_data = HistoryFilter(
            data=request.query_params,
            queryset=queryset
        )
        serializer = self.get_serializer(filtered_data.qs, many=True)
        return Response({"result": "success", "data": serializer.data})
