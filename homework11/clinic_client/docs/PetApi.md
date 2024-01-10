# clinic_api.PetApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pet_create**](PetApi.md#pet_create) | **POST** /pet/create | Create
[**pet_delete**](PetApi.md#pet_delete) | **DELETE** /pet/delete/{pet_id} | Delete
[**pet_get_all**](PetApi.md#pet_get_all) | **GET** /pet/get-all | Get All
[**pet_get_by_id**](PetApi.md#pet_get_by_id) | **GET** /pet/get/{pet_id} | Get By Id
[**pet_update**](PetApi.md#pet_update) | **PUT** /pet/update | Update

# **pet_create**
> PetOut pet_create(body)

Create

### Example
```python
from __future__ import print_function
import time
import clinic_api
from clinic_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clinic_api.PetApi()
body = clinic_api.PetIn() # PetIn | 

try:
    # Create
    api_response = api_instance.pet_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PetApi->pet_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PetIn**](PetIn.md)|  | 

### Return type

[**PetOut**](PetOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pet_delete**
> object pet_delete(pet_id)

Delete

### Example
```python
from __future__ import print_function
import time
import clinic_api
from clinic_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clinic_api.PetApi()
pet_id = NULL # object | 

try:
    # Delete
    api_response = api_instance.pet_delete(pet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PetApi->pet_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pet_get_all**
> object pet_get_all()

Get All

### Example
```python
from __future__ import print_function
import time
import clinic_api
from clinic_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clinic_api.PetApi()

try:
    # Get All
    api_response = api_instance.pet_get_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PetApi->pet_get_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pet_get_by_id**
> PetOut pet_get_by_id(pet_id)

Get By Id

### Example
```python
from __future__ import print_function
import time
import clinic_api
from clinic_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clinic_api.PetApi()
pet_id = NULL # object | 

try:
    # Get By Id
    api_response = api_instance.pet_get_by_id(pet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PetApi->pet_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pet_id** | [**object**](.md)|  | 

### Return type

[**PetOut**](PetOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pet_update**
> PetOut pet_update(body)

Update

### Example
```python
from __future__ import print_function
import time
import clinic_api
from clinic_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clinic_api.PetApi()
body = clinic_api.PetUpdate() # PetUpdate | 

try:
    # Update
    api_response = api_instance.pet_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PetApi->pet_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PetUpdate**](PetUpdate.md)|  | 

### Return type

[**PetOut**](PetOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

