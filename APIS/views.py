# from django.http import JsonResponse
# from django.shortcuts import render
from rest_framework.response import Response
from students.models import Student
from .serializers import StudentsSerializer
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

# manual serilazation way
# def studentsView(request):
#     students = Student.objects.all() 
#     student_list = list(students.values())
#     return JsonResponse(student_list, safe=False)

@api_view(['GET', 'POST'])
def studentsView(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentsSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def studentDetailView(request, pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serilalizer = StudentsSerializer(student) 
            return Response(serilalizer.data,  status=status.HTTP_200_OK) 

        elif request.method == 'PUT':
            serializer = StudentsSerializer(student,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:    
              return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


        elif request.method == 'DELETE':
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
         