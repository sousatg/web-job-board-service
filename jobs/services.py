import uuid
from datetime import datetime

from .models import Job
from .models import Company

class JobService:
    @staticmethod
    def get_job(*, job_id: uuid.UUID):
        job = Job.objects.get(id=job_id)

        return job

    @staticmethod
    def list_jobs():
        jobs = Job.objects.all()

        return jobs

    @staticmethod
    def create_job(
        title: str, 
        description: str,
        application_link: str,
        posted_at: str,
        posted_on: datetime,
        company_id: uuid.UUID
    ):
        company = CompanyService.get_company(company_id)

        job = Job(
            title=title, 
            description=description, 
            application_link=application_link,
            posted_at=posted_at,
            posted_on=posted_on,
            company=company
        )

        job.save()

        return job

class CompanyService:
    @staticmethod
    def list_companies():
        return Company.objects.all()

    @staticmethod
    def get_company(company_id: uuid.UUID):
        company = Company.objects.get(id=company_id)

        return company

    @staticmethod
    def create_company(*, name: str, website: str):
        company = Company(name=name, website=website)
        company.save()

        return company

    
