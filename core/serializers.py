from rest_framework import serializers
from .models import MedicalDepartment, SelfDiagnosis, Symtom, Treatment, Disease

class MedicalDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalDepartment
        fields = '__all__'


class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = '__all__'
