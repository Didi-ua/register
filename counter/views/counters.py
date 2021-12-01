from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers.counters import CounterSerializer
from .serializers.history import HistorySerializer
from counter.models import History


class CounterViewSet(ModelViewSet):
    serializer_class = CounterSerializer

    def get_queryset(self):
        return self.request.user.counters.all()

    @action(detail=True, methods=['get'], serializer_class=HistorySerializer)
    def history(self, request, pk=None):
        queryset = History.objects.filter(counter=self.get_object())
        serializer = HistorySerializer(queryset, many=True)
        return Response({"result": "success", "data": serializer.data})
