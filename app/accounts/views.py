from django.core.files import File
from django.db.models import Q
from rest_framework.views import APIView
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import (
    TableSerializer,
    # ChangePasswordSerializer,
    TableDetailSerializer,


)
from .models import Table
from datetime import datetime
from rest_framework.generics import (
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView
)
# from django.conf.settings import STATIC_ROOT

class table_get(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TableSerializer
    # search_fields = []
    
    def get_queryset(self, *args, **kwargs):
        queryset_list = Table.objects.all()
        # .order_by('-id')[:10]
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                # Q(Run_status__icontains=query) |
                Q(Date_time__icontains=query) |
                Q(Run_status__icontains=query)
            ).distinct()
        else:
            queryset_list = queryset_list.order_by('-id')[:10]

        return queryset_list
        


class ReadFile(APIView):
    # authentication_classes=[Token]
    # lookup_field = 'id'
    # queryset = Table.objects.all
    permission_classes = [IsAuthenticated]
    serializer_class = TableDetailSerializer

    def post(self,request):
        paths = self.request.data['path']
        print(paths)
        f = open(paths,'r')
        readtxt = f.read()
        print(readtxt)
        return Response(readtxt)    

    # def post(self, request):
    #     path = Table.objects.get(path=path)
    #     print(path)
    #     return Response(path)
    


# class ChangePasswordView(UpdateAPIView):
#     serializer_class = ChangePasswordSerializer

    # def update(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.save()
    #     # if using drf authtoken, create a new token
    #     if hasattr(user, 'auth_token'):
    #         user.auth_token.delete()
    #     token, created = Token.objects.get_or_create(user=user)
    #     # return new token
    #     return Response({'token': token.key}, status=status.HTTP_200_OK)
