import logging
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Company
from .models import Job
from .services import CompanyService
from .services import JobService

logger = logging.getLogger(__name__)

class JobListApi(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Job
            fields = "__all__"

    def get(self, request):
        logger.info("method 'list' called")

        jobs = JobService.list_jobs()

        serializer = self.OutputSerializer(jobs, many=True)

        return Response(serializer.data)

class JobDetailsAPI(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Job
            fields = "__all__"

    def get(self, request, job_id):
        logger.info("method 'list' called")

        job = JobService.get_job(job_id=job_id)

        serializer = self.OutputSerializer(job, many=False)

        return Response(serializer.data)

class JobCreateAPI(APIView):
    class InputSerializer(serializers.Serializer):
        title = serializers.CharField()
        description = serializers.CharField()
        application_link = serializers.CharField()
        posted_at = serializers.CharField()
        posted_on = serializers.DateField()
        company_id = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        JobService.create_job(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)

class CompanyListAPI(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Company
            fields = ("id", "name", "website")

    def get(self, request):
        logger.info("method 'get' called")

        companies = CompanyService.list_companies()

        serializer = self.OutputSerializer(companies, many=True)

        return Response(serializer.data)

class CompanyGetAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        name = serializers.CharField()
        website = serializers.CharField()

    def get(self, request, company_id):
        logger.info("method 'get' called")

        company = CompanyService.get_company(company_id=company_id)

        serializer = self.OutputSerializer(company, many=False)

        return Response(serializer.data)

class CompanyCreateAPI(APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        website = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        CompanyService.create_company(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)