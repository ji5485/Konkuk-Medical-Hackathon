from django.urls import path
from . import views

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title="My API")

urlpatterns = [
    path('', schema_view),
    path('data_generator/', views.dummy_data, name="data_generator"),
    path('delete_dept/', views.delete_dept, name="delete_dept"),
    path('api/dept/', views.MedicalDepartmentClass.as_view(), name="medical_department"),
    path('api/diag/', views.SelfDiagnosisClass.as_view(), name="self_diagnosis"),
    path('api/treatment/', views.TreatmentClass.as_view(), name="treatment")
]

