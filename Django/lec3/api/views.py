from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from .models import Student, Kitten
from .serializers import StudentSerializer
from rest_framework.views import APIView
from .serializers import KittenSerializer
from .models import Kitten

@api_view(['GET', 'PUT', 'DELETE']) #/students/3
def edit_student(request: Request, id:int):
    if request.method == 'GET':
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    if request.method == 'DELETE':
        student = Student.objects.get(id=id)
        student.delete()
        return Response({'message' : 'Student Deleted'},status=204)

    if request.method == 'PUT':
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
@api_view(['GET', 'POST'])
def index(request:Request):
    
    if request.method == 'POST':
        # serializer is in create mode:
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save() # will invoke create
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response({'students': serializer.data})



class KittenViews(APIView):
    def get(self, request):
        kittens = Kitten.objects.all()
        serializer = KittenSerializer(kittens, many = True)
        return Response({"kittens": serializer.data})

    def post(self, request):
        kitten = KittenSerializer(data = request.data)

        if kitten.is_valid():
            kitten.save() 
            return Response(kitten.data, status = 201)
        else:
            return Response({"errors": kitten.errors}, status = 400)
        