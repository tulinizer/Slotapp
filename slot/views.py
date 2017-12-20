import json

from django.db.models import Q
from django.core.serializers.json import DjangoJSONEncoder

from rest_framework import viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response

from slot.serializers import EmployeeSlotSerializer, CandidateSlotSerializer, EmployeeSerializer, CandidateSerializer
from .models import Candidate, Employee, CandidateSlot, EmployeeSlot


def find_intersection(s1, s2):
    if max(s1.start_date, s2.start_date) != min(s1.end_date, s2.end_date):

        return {'start_date': max(s1.start_date, s2.start_date), 'end_date': min(s1.end_date, s2.end_date)}
    return None


class EmployeeSlotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = EmployeeSlot.objects.all().order_by('start_date')
    serializer_class = EmployeeSlotSerializer


class CandidateSlotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CandidateSlot.objects.all().order_by('start_date')
    serializer_class = CandidateSlotSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    @detail_route(url_name='search', url_path='search/(?P<employee_id>[0-9]+)')
    def search(self, request, pk=None, employee_id=None):

        c = self.get_object()
        e = Employee.objects.get(id=employee_id)

        slot_list = []
        for slot in c.slots.all():
            qset = e.slots.filter(
                Q(end_date__lte=slot.end_date, end_date__gte=slot.start_date) | Q(start_date__lte=slot.end_date,
                                                                                start_date__gte=slot.start_date))
            for q in qset:
                intersection = find_intersection(slot, q)
                if intersection is not None:
                    slot_list.append(intersection)

        return Response(json.dumps(slot_list, cls=DjangoJSONEncoder))
