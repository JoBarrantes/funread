from django.shortcuts import render
import json
from wsgiref import headers
from .models import Institute,InstituteMembers
from .serializers import InstituteSerializer, InstituteMembersSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import hashlib
import sys
sys.path.append('funread_backend')
import verifyJwt

# -----------------Institute----------------------------

@api_view(['POST'])
def createInstitute(request):

    #token verification
    authorization_header = request.headers.get('Authorization')
    verify = verifyJwt.JWTValidator(authorization_header)
    es_valido = verify.validar_token()
    if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    data = {
        
        'name': request.data.get('name').lower(),
        
        }
    serializer = InstituteSerializer(data=data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response({"msg":"Almacenado con exito","data":serializer.data}, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def listedInstitute(request):

    #token verification
    authorization_header = request.headers.get('Authorization')
    verify = verifyJwt.JWTValidator(authorization_header)
    es_valido = verify.validar_token()
    if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    institute=Institute.objects.all()
    serializer = InstituteSerializer(institute, many=True)
    return Response(serializer.data)










@api_view(['PUT'])
def instituteChange(request):

    #token verification
    authorization_header = request.headers.get('Authorization')
    verify = verifyJwt.JWTValidator(authorization_header)
    es_valido = verify.validar_token()
    if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    institute = Institute.objects.get(name=request.data.get("name"))
    data={
        "name":request.data.get("change"),
        
        
    }
    serializer = InstituteSerializer(institute, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['DELETE'])
def deleteInstitute(request):

    #token verification
    authorization_header = request.headers.get('Authorization')
    verify = verifyJwt.JWTValidator(authorization_header)
    es_valido = verify.validar_token()
    if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    institute = Institute.objects.get(instituteId=request.data.get("instituteId"))
    institute.delete()
    return Response({"msj":"successfully delete"},status=status.HTTP_200_OK)





#-----------------InstituteMembers----------------------------
#'InstituteID', 'UserId'

@api_view(['POST'])
def createMembers(request):

    #token verification
    authorization_header = request.headers.get('Authorization')
    verify = verifyJwt.JWTValidator(authorization_header)
    es_valido = verify.validar_token()
    if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    data = {
        
        'userId': request.data.get('userId'),
        'instituteId': request.data.get('instituteId'),
        
        }
    serializer = InstituteMembersSerializer(data=data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response({"msg":"successfully stored","data":serializer.data}, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def listedMembers(request):

    #token verification
    authorization_header = request.headers.get('Authorization')
    verify = verifyJwt.JWTValidator(authorization_header)
    es_valido = verify.validar_token()
    if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    instituteMembers=InstituteMembers.objects.all()
    serializer = InstituteMembersSerializer(instituteMembers, many=True)
    return Response(serializer.data)



@api_view(['PUT'])
def memberChange(request):

    #token verification
    authorization_header = request.headers.get('Authorization')
    verify = verifyJwt.JWTValidator(authorization_header)
    es_valido = verify.validar_token()
    if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    instituteMembers = InstituteMembers.objects.get(instituteMembersId=request.data.get("instituteMembersId"))
    data={
        "userId":request.data.get("userchange"),
        "instituteId":request.data.get("institutechange"),
        
        
    }
    serializer = InstituteMembersSerializer(instituteMembers, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteMembers(request):

    #token verification
    authorization_header = request.headers.get('Authorization')
    verify = verifyJwt.JWTValidator(authorization_header)
    es_valido = verify.validar_token()
    if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    instituteMembers = InstituteMembers.objects.get(instituteMembersId=request.data.get("instituteMembersId"))
    instituteMembers.delete()

    return Response({"msj":"successfully delete"},status=status.HTTP_200_OK)