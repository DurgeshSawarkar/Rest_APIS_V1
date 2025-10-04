# from django.http import JsonResponse
# from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from students.models import Student
from .serializers import StudentsSerializer, EmployeeSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employee.models import Employee
from rest_framework import mixins, generics, viewsets
from blog.models import Blog, Comment
from blog.serializers import BlogSerializer, CommentSerializer
from .pagination import CustomPagination
from employee.filters import EmployeeFilter
from rest_framework.filters import SearchFilter, OrderingFilter
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
         

# class Employees(APIView):
#              def get(self, request):
#                 employees = Employee.objects.all()
#                 serializer = EmployeeSerializer(employees, many=True)
#                 return Response(serializer.data, status=status.HTTP_200_OK)
             
#              def post(self, request):
#                   serializer = EmployeeSerializer(data=request.data)
#                   if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data, status=status.HTTP_201_CREATED)
#                   else:
#                     return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
                  
            
                  

# class EmmployeesDetail(APIView):

    # def get_object(self,pk):
    #     try:
    #         return Employee.objects.get(pk=pk)
    #     except Employee.DoesNotExist:
    #         raise Http404
        

    # def get(self, request, pk):
    #     employee =  self.get_object(pk)
    #     serializer = EmployeeSerializer(employee)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # def put(self, request, pk):
    #     employee =  self.get_object(pk)
    #     serializer = EmployeeSerializer(employee, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk):
    #     employee = self.get_object(pk)
    #     employee.delete()    
    #     return Response(status=status.HTTP_204_NO_CONTENT)




# #mixins
# class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class =EmployeeSerializer

#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)
    
# class EmmployeesDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class =EmployeeSerializer

#     def get(self,request,pk):
#         return self.retrieve(request, pk)
    
#     def put(self,request,pk):
#         return self.update(request,pk)
    
#     def delete(self,request,pk):
#         return self.destroy(request,pk)


"""
#Generics
class Employees(generics.ListAPIView, generics.CreateAPIView):
      queryset = Employee.objects.all()
      serializer_class =EmployeeSerializer
    

class EmmployeesDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
      queryset = Employee.objects.all()
      serializer_class =EmployeeSerializer    
      lookup_field ="pk"

      """

# class EmployeeViewset(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Employee.objects.all()
#         serializer = EmployeeSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        

#     def  retrieve(self, request, pk=None):
#         employee = get_object_or_404(Employee, pk=pk)
#         serializer = EmployeeSerializer(employee) 
#         return Response(serializer.data)
    
#     def update(self, request, pk=None):
#         employee = get_object_or_404(Employee, pk=pk)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
#     def delete(self, request, pk=None):
#          employee = get_object_or_404(Employee, pk=pk)
#          employee.delete()
#          return Response(status=status.HTTP_204_NO_CONTENT)
        

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination
    filterset_class = EmployeeFilter



class BlogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields  = ['^blog_title', ['blog_body']]
    ordering_fields = ['id']
   


class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class BlogDetailview(generics.RetrieveUpdateDestroyAPIView):
    queryset =Blog.objects.all()
    serializer_class =BlogSerializer
    lookup_field ='pk'
  


class CommentDetailview(generics.RetrieveUpdateDestroyAPIView):
      queryset =Comment.objects.all()
      serializer_class =CommentSerializer
      lookup_field ='pk'