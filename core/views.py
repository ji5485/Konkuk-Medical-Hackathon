from django.shortcuts import render
from django.http import HttpResponse
from .models import MedicalDepartment, SelfDiagnosis, Symtom, Treatment, Disease


def delete_dept(request):
    MedicalDepartment.objects.all().delete()
    
def dummy_data(request):
    delete_dept(request)

    medical_dept_list = ['가정의학과', '감염내과','건강의학과', '내분비대사내과','루마티스내과','마취통증의학과', '방사선종양학과', '병리과','비뇨의학과','산부인과','성형외과','소아청소년과','소화기내과','신경과','신경외과','신장내과','심장혈관내과','안과','영상의학과','외과','응급의학과','이비인후-두경부외과','임상약리학과','재활의학과','정형외과','종양혈액내과','진단검사의학과','치과','피부과','핵의학과','호흡기-알레르기내과','흉부외과']

    for medical_dept in medical_dept_list:
        MedicalDepartment.objects.create(name=medical_dept,base_fare=16450)


    treatment_dict = {"혈액검사": 40000,"흉부 방사선 촬영":15000,"흉부 MRI":420000,"흉부 전산화 단층 촬영":250000,"기관지 내시경":306000}

    medical_department = MedicalDepartment.objects.get(name="가정의학과")

    for name,price in treatment_dict.items():
        treatment = Treatment(name=name,price=price)
        treatment.save()
        treatment.department.add(medical_department)
    
    return HttpResponse("데이터가 생성되었습니다.")

def main(request):

    return render(request, 'core/main.html')


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MedicalDepartmentSerializer,TreatmentSerializer
import json
from django.core import serializers


# Create your views here.

class MedicalDepartmentClass(APIView):
    # MedicalDepartment 조회
    def get(self, request, format=None):
        queryset = MedicalDepartment.objects.all()
        serializer = MedicalDepartmentSerializer(queryset, many=True)
        return Response(serializer.data)

    # MedicalDepartment 선택
    def post(self, request, format=None):
        medical_department = MedicalDepartment.objects.get(name=request.data.get('department'))
        queryset = Disease.objects.filter(department=medical_department)
        serializer = TreatmentSerializer(queryset,many=True)

        ##medical_department = serializers.serialize('json',[medical_department,])

        context = {
            'medical_department':medical_department.name,
            'disease_list':serializer.data
        }
        return Response(context)

    # 전화번호부 아이템 제거
    def delete(self, request, format=None):
        id = request.data.get('id')
        post = Phone.objects.get(id=id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SelfDiagnosisClass(APIView):
    def post(self, request, format=None):
        department_name = request.data.get('department')
        department = MedicalDepartment.objects.get(name=department_name)

        symtom_list = request.data.get('symtom_list')
        medicine = request.data.get('medicine')
        is_visited = request.data.get('is_visited')
        is_rediagnose = request.data.get('is_rediagnose')
        opinion = request.data.get('opinion')

        self_diagnosis = SelfDiagnosis(
            department=department,
            opinion=opinion,
            is_visited=is_visited,
            is_rediagnose=is_rediagnose,
            medicine=medicine,
        )
        
        self_diagnosis.save()

        for symtom in symtom_list:
            name = symtom['name']
            disease = Disease.objects.get(name=name)
            period = symtom['period']
            degree = symtom['degree']
            Symtom.objects.create(self_diagnosis=self_diagnosis,name=disease,period=period,degree=degree)

        return Response(status=status.HTTP_200_OK)

# {
#     "department": "가정의학과",
#     "symtom_list":[
#         {
#             "name": "기침",
#             "period": "1주",
#             "degree": 3
#         },
#         {
#             "name": "발열",
#             "period": "1주",
#             "degree": 3
#         }
#     ],
#     "medicine": "해열제,진통소염제",
#     "is_visited": false,
#     "is_rediagnose": true,
#     "opinion": "동네 병원을 가도 치료의 진전이 없습니다."
# }