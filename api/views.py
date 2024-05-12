from . import serializers
from main import models
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def home(request):
    data = models.Home.objects.all()
    serializer = serializers.HomeSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def portfolio(request):
    data = models.Portfolio.objects.all()
    serializer = serializers.PortfolioSerializer(data, many=True)
    return Response(serializer.data)



@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def team(request):
    data = models.Team.objects.all()
    serializer = serializers.TeamSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def team_member(request):
    data = models.TeamMember.objects.all()
    serializer = serializers.TeamMemberSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def service(request):
    data = models.Service.objects.all()
    serializer = serializers.ServiceSerializer(data, many=True)
    return Response(serializer.data)



@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def vacancy(request):
    data = models.Vacancies.objects.all()
    serializer = serializers.VacanciesSerializer(data, many=True)
    return Response(serializer.data)




@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def vacancies_list(request):
    data = models.VacanciesList.objects.all()
    serializer = serializers.VacanciesListSerializer(data, many=True)
    return Response(serializer.data)




@api_view(['POST','GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def vacancies_resume_create(request):
    if request.method == 'POST':
        serializer = serializers.VacancyResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    elif request.method == 'GET':
        data = models.VacancyResume.objects.all()
        serializer = serializers.VacancyResumeSerializer(data, many=True)
        return Response(serializer.data)
    


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def message_create(request):
    if request.method == 'POST':
        serializer = serializers.MassageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)









