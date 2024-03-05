from django.shortcuts import render
from CarDekhoApp.models import *
from django.http import JsonResponse, HttpResponse
from pprint import pprint
import json
from .api_file.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,DjangoModelPermissions
from rest_framework import mixins, generics
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# def car_list_view(request):
#     cars = Carlist.objects.all()
#     data = {
#         'cars': list(cars.values()),
#     }
#     print(type(data))
#     data_json = json.dumps(data)
#     print(type(data_json))
#     return HttpResponse(data_json,content_type='application/json')
#     # return JsonResponse(data)


# def car_detail_view(request,pk):
#     car = Carlist.objects.get(pk = pk)
#     data = {
#         'name' : car.name,
#         'description': car.description,
#         'active':car.active
#     }
#     return JsonResponse(data)


class ReviewDetails(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class Showroom_Viewset(viewsets.ModelViewSet):
    queryset = Showroomlist.objects.all()
    serializer_class = ShowroomSerializer


# class Showroom_Viewset(viewsets.ViewSet):
#     def list(self,request):
#         queryset = Showroomlist.objects.all()
#         serializer = ShowroomSerializer(queryset,many = True)
#         return Response(serializer.data)
    
#     def retrieve(self,request,pk=None):
#         queryset = Showroomlist.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = ShowroomSerializer(user)
#         return Response(serializer.data)


#     def create(self,request):
#         serializer = ShowroomSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class Showroom_View(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        showroom = Showroomlist.objects.all()
        serializer = ShowroomSerializer(showroom, many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ShowroomSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class Showroom_Details(APIView):
    def get(self,request,pk):
        try:
            showroom = Showroomlist.objects.get(pk=pk)
        except Showroomlist.DoesNotExist:
            return Response({'Error':'showroom not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ShowroomSerializer(showroom)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        try:
            showroom = Showroomlist.objects.get(pk=pk)
        except Showroomlist.DoesNotExist:
            return Response({'Error':'showroom not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ShowroomSerializer(showroom,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,pk):
        try:
            showroom = Showroomlist.objects.get(pk=pk)
        except Showroomlist.DoesNotExist:
            return Response({'Error':'showroom not found'}, status=status.HTTP_404_NOT_FOUND)
        showroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





@api_view(['GET','POST'])
def car_list_view(request):

    if request.method == 'GET':
        print("This is get")
        cars = Carlist.objects.all()
        serializer = CarSerializer(cars,many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print("This is post")
        serializer = CarSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET','PUT','DELETE'])
def car_detail_view(request,pk):
    if request.method == 'GET':
        try:
            car = Carlist.objects.get(pk=pk)
        except:
            return Response({'Error':'car not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        try:
            car = Carlist.objects.get(pk=pk)
        except:
            return Response({'Error':'car not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    if request.method == 'DELETE':
        car =  Carlist.objects.get(pk=pk)
        car.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)