# coding: utf-8

# flake8: noqa

"""
    Clinic Service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from clinic_api.api.client_api import ClientApi
from clinic_api.api.consultation_api import ConsultationApi
from clinic_api.api.pet_api import PetApi
# import ApiClient
from clinic_api.api_client import ApiClient
from clinic_api.configuration import Configuration
# import models into sdk package
from clinic_api.models.client_in import ClientIn
from clinic_api.models.client_out import ClientOut
from clinic_api.models.client_update import ClientUpdate
from clinic_api.models.consultation_in import ConsultationIn
from clinic_api.models.consultation_out import ConsultationOut
from clinic_api.models.consultation_update import ConsultationUpdate
from clinic_api.models.http_validation_error import HTTPValidationError
from clinic_api.models.pet_in import PetIn
from clinic_api.models.pet_out import PetOut
from clinic_api.models.pet_update import PetUpdate
from clinic_api.models.validation_error import ValidationError
