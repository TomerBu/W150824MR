from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import FunFact
from .serializers import FunFactsSerializer

class FunFactsView(APIView):
    def get(self, request: Request):
        facts = FunFact.objects.all()
        serializer = FunFactsSerializer(facts, many=True)
        return Response({'facts': serializer.data})

    def post(self, request: Request):
        serializer = FunFactsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class FactsDetailsView(APIView):
    def get(self, request: Request, pk: int):
        try:
            fact = FunFact.objects.get(pk=pk)
        except FunFact.DoesNotExist:
            return Response(
                {'message': f'Fact with id {pk} not found'},
                status=404
            )
       
        serializer = FunFactsSerializer(fact)
        return Response({'facts': serializer.data})
    
    def delete(self, request: Request, pk: int):
        try:
            fact = FunFact.objects.get(pk=pk)
        except FunFact.DoesNotExist:
            return Response(
                {'message': f'Fact with id {pk} not found'},
                status=404
            )
        fact.delete()
        return Response(status=204)
    
    def put(self, request: Request, pk: int): 
        try:
            fact = FunFact.objects.get(pk=pk)
        except FunFact.DoesNotExist:
            return Response(
                {'message': f'Fact with id {pk} not found'},
                status=404
            )
        serializer = FunFactsSerializer(fact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'errors':serializer.errors}, status = 400)