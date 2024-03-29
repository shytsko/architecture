# clinic-api
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import clinic_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import clinic_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import clinic_api
from clinic_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clinic_api.ClientApi(clinic_api.ApiClient(configuration))
body = clinic_api.ClientIn() # ClientIn | 

try:
    # Create
    api_response = api_instance.client_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->client_create: %s\n" % e)

# create an instance of the API class
api_instance = clinic_api.ClientApi(clinic_api.ApiClient(configuration))
client_id = NULL # object | 

try:
    # Delete
    api_response = api_instance.client_delete(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->client_delete: %s\n" % e)

# create an instance of the API class
api_instance = clinic_api.ClientApi(clinic_api.ApiClient(configuration))

try:
    # Get All
    api_response = api_instance.client_get_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->client_get_all: %s\n" % e)

# create an instance of the API class
api_instance = clinic_api.ClientApi(clinic_api.ApiClient(configuration))
client_id = NULL # object | 

try:
    # Get By Id
    api_response = api_instance.client_get_by_id(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->client_get_by_id: %s\n" % e)

# create an instance of the API class
api_instance = clinic_api.ClientApi(clinic_api.ApiClient(configuration))
body = clinic_api.ClientUpdate() # ClientUpdate | 

try:
    # Update
    api_response = api_instance.client_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->client_update: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ClientApi* | [**client_create**](docs/ClientApi.md#client_create) | **POST** /client/create | Create
*ClientApi* | [**client_delete**](docs/ClientApi.md#client_delete) | **DELETE** /client/delete/{client_id} | Delete
*ClientApi* | [**client_get_all**](docs/ClientApi.md#client_get_all) | **GET** /client/get-all | Get All
*ClientApi* | [**client_get_by_id**](docs/ClientApi.md#client_get_by_id) | **GET** /client/get/{client_id} | Get By Id
*ClientApi* | [**client_update**](docs/ClientApi.md#client_update) | **PUT** /client/update | Update
*ConsultationApi* | [**consultation_create**](docs/ConsultationApi.md#consultation_create) | **POST** /consultation/create | Create
*ConsultationApi* | [**consultation_delete**](docs/ConsultationApi.md#consultation_delete) | **DELETE** /consultation/delete/{consultation_id} | Delete
*ConsultationApi* | [**consultation_get_all**](docs/ConsultationApi.md#consultation_get_all) | **GET** /consultation/get-all | Get All
*ConsultationApi* | [**consultation_get_by_id**](docs/ConsultationApi.md#consultation_get_by_id) | **GET** /consultation/get/{consultation_id} | Get By Id
*ConsultationApi* | [**consultation_update**](docs/ConsultationApi.md#consultation_update) | **PUT** /consultation/update | Update
*PetApi* | [**pet_create**](docs/PetApi.md#pet_create) | **POST** /pet/create | Create
*PetApi* | [**pet_delete**](docs/PetApi.md#pet_delete) | **DELETE** /pet/delete/{pet_id} | Delete
*PetApi* | [**pet_get_all**](docs/PetApi.md#pet_get_all) | **GET** /pet/get-all | Get All
*PetApi* | [**pet_get_by_id**](docs/PetApi.md#pet_get_by_id) | **GET** /pet/get/{pet_id} | Get By Id
*PetApi* | [**pet_update**](docs/PetApi.md#pet_update) | **PUT** /pet/update | Update

## Documentation For Models

 - [ClientIn](docs/ClientIn.md)
 - [ClientOut](docs/ClientOut.md)
 - [ClientUpdate](docs/ClientUpdate.md)
 - [ConsultationIn](docs/ConsultationIn.md)
 - [ConsultationOut](docs/ConsultationOut.md)
 - [ConsultationUpdate](docs/ConsultationUpdate.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [PetIn](docs/PetIn.md)
 - [PetOut](docs/PetOut.md)
 - [PetUpdate](docs/PetUpdate.md)
 - [ValidationError](docs/ValidationError.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author


