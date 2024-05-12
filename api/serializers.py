from main import models
from rest_framework import serializers


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Home
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Portfolio
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        fields = '__all__'


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeamMember
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'


class VacanciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vacancies
        fields = '__all__'        


class VacanciesSerializerList(serializers.ModelSerializer):
    class Meta:
        model = models.Vacancies
        fields = ['name', 'working_days', 'start_working', 'end_working', 'salary', ]


class VacancyResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VacancyResume
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = ['name', 'phone', 'message']


