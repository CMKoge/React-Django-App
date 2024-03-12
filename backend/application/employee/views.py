from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializer import *

# Create your views here.
class ReactView(APIView):
    """
    A simple View that returns a list of all employees.
    """
    def get(self, request):
        output = [{"name":output.name, "dept":output.department} for output in Employee.objects.all()]
        return Response(output)
    
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    
    