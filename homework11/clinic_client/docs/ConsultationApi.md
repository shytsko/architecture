# clinic_api.ConsultationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consultation_create**](ConsultationApi.md#consultation_create) | **POST** /consultation/create | Create
[**consultation_delete**](ConsultationApi.md#consultation_delete) | **DELETE** /consultation/delete/{consultation_id} | Delete
[**consultation_get_all**](ConsultationApi.md#consultation_get_all) | **GET** /consultation/get-all | Get All
[**consultation_get_by_id**](ConsultationApi.md#consultation_get_by_id) | **GET** /consultation/get/{consultation_id} | Get By Id
[**consultation_update**](ConsultationApi.md#consultation_update) | **PUT** /consultation/update | Update

# **consultation_create**
> ConsultationOut consultation_create(body)

Create

### Example
```python
from __future__ import print_function
import time
import clinic_api
from clinic_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clinic_api.ConsultationApi()
body = clinic_api.ConsultationIn() # ConsultationIn | 

try:
    # Create
    api_response = api_instance.consultation_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsultationApi->consultation_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConsultationIn**](ConsultationIn.md)|  | 

### Return type

[**ConsultationOut**](ConsultationOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consultation_delete**
> object consultation_delete(consultation_id)

Delete

### Example
```python
from __future__ import print_function
import time
import clinic_api
from clinic_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clinic_api.ConsultationApi()
consultation_id = NULL # object | 

try:
    # Delete
    api_response = api_instance.consultation_delete(consultation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsultationApi->consultation_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consultation_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consultation_get_all**
> object consultation_get_all()

Get All

### Example
```python
from __future__ import print_function
import time
import clinic_api
from clinic_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clinic_api.ConsultationApi()

try:
    # Get All
    api_response = api_instance.consultation_get_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsultationApi->consultation_get_all: %s\n" % e)
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

# **consultation_get_by_id**
> ConsultationOut consultation_get_by_id(consultation_id)

Get By Id

### Example
```python
from __future__ import print_function
import time
import clinic_api
from clinic_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clinic_api.ConsultationApi()
consultation_id = NULL # object | 

try:
    # Get By Id
    api_response = api_instance.consultation_get_by_id(consultation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsultationApi->consultation_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consultation_id** | [**object**](.md)|  | 

### Return type

[**ConsultationOut**](ConsultationOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consultation_update**
> ConsultationOut consultation_update(body)

Update

### Example
```python
from __future__ import print_function
import time
import clinic_api
from clinic_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clinic_api.ConsultationApi()
body = clinic_api.ConsultationUpdate() # ConsultationUpdate | 

try:
    # Update
    api_response = api_instance.consultation_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsultationApi->consultation_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConsultationUpdate**](ConsultationUpdate.md)|  | 

### Return type

[**ConsultationOut**](ConsultationOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

