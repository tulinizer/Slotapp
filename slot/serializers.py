from .models import EmployeeSlot, CandidateSlot, Employee, Candidate
from rest_framework import serializers


class EmployeeSlotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmployeeSlot
        fields = ('employee', 'start_date', 'end_date')


class CandidateSlotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CandidateSlot
        fields = ('candidate', 'start_date', 'end_date')


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('name',)


class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidate
        fields = ('name',)
