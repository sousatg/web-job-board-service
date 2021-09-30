from django.urls import path
from rest_framework.routers import DefaultRouter

from .apis import CompanyCreateAPI
from .apis import CompanyGetAPI
from .apis import CompanyListAPI
from .apis import JobCreateAPI
from .apis import JobDetailsAPI
from .apis import JobListApi

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    # path('', include(router.urls)),
    path("companies", CompanyListAPI.as_view(), name="company"),
    path("companies", CompanyCreateAPI.as_view(), name="company"),
    path("companies/<str:company_id>", CompanyGetAPI.as_view(), name="company"),
    path("jobs", JobListApi.as_view(), name="job"),
    path("jobs", JobCreateAPI.as_view(), name="job"),
    path("jobs/<str:job_id>", JobDetailsAPI.as_view(), name="job"),
]

urlpatterns += router.urls
