from yaml import serialize
from office_app.api.serializers import PatientSerializer, VitalsSerializer
from office_app.models import Patient, Vitals
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .serializers import PatientSerializer


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
    


class VitalsListCreateAPIView(APIView):
    
    def get(self, request):
        vitals = Vitals.objects.all().order_by('-id')
        serializer = VitalsSerializer(vitals,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = VitalsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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