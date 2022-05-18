from office_app.models import (Doctors, Patient, Vitals, Diagnosis,
                                    Prescription, Bills, Appointments)
from rest_framework import generics, mixins, status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (PatientSerializer, PrescriptionSerializer,
                            VitalsSerializer, DoctorsSerializer, 
                            DiagnosisSerializer)


@api_view(['GET'])
def patient_list_create_api_view(request):
    if request.method == 'GET':
        patient = Patient.objects.all()
        serializer = PatientSerializer(patient, many=True)
        return Response(serializer.data)


class PatientListCreateAPIView(APIView):

    def get(self, request):
        patient = Patient.objects.all().order_by('id')
        serializer = PatientSerializer(patient,
                                        many=True,
                                        context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientDetailView(APIView):

    def get_object(self, pk):
        patient = get_object_or_404(Patient, pk=pk)
        return patient

    def get(self, request, pk):
        patient = self.get_object(pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk):
        patient = self.get_object(pk)
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        patient = self.get_object(pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class VitalsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vitals.objects.all()
    serializer_class = VitalsSerializer


# class VitalsListCreateAPIView(APIView):
    
#     def get(self, request):
#         vitals = Vitals.objects.all().order_by('-id')
#         serializer = VitalsSerializer(vitals,many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = VitalsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VitalsDetailView(APIView):
    def get_object(self, pk):
        vitals = get_object_or_404(Vitals, pk=pk)
        return vitals

    def get(self, request, pk):
        vitals = self.get_object(pk)
        serializer = VitalsSerializer(vitals)
        return Response(serializer.data)

    def put(self, request, pk):
        vitals = self.get_object(pk)
        serializer = VitalsSerializer(vitals, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        vitals = self.get_object(pk)
        vitals.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DoctorsListCreateAPIView(mixins.ListModelMixin,
                                mixins.CreateModelMixin,
                                generics.GenericAPIView):
    
    queryset = Doctors.objects.all()
    serializer_class = DoctorsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DoctorsRetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                            mixins.UpdateModelMixin,
                                            mixins.DestroyModelMixin,
                                            generics.GenericAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorsSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class DiagnosisListCreateAPIView(generics.ListCreateAPIView):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer

    def perform_create(self, serializer):
        patient_pk = self.kwargs.get('patient_pk')
        patient = get_object_or_404(Patient, pk=patient_pk)
        serializer.save(patient=patient)

class DiagnosisDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer


class PrescriptionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

    def perform_create(self, serializer):
        patient_pk = self.kwargs.get('patient_pk')
        patient = get_object_or_404(Patient, pk=patient_pk)
        serializer.save(patient=patient)

class PrescriptionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer