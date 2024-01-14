# clinic_api.ClientApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**client_create**](ClientApi.md#client_create) | **POST** /client/create | Create
[**client_delete**](ClientApi.md#client_delete) | **DELETE** /client/delete/{client_id} | Delete
[**client_get_all**](ClientApi.md#client_get_all) | **GET** /client/get-all | Get All
[**client_get_by_id**](ClientApi.md#client_get_by_id) | **GET** /client/get/{client_id} | Get By Id
[**client_update**](ClientApi.md#client_update) | **PUT** /client/update | Update

# **client_create**
> ClientOut client_create(body)

Create

### Example
```python
from __future__ import print_function
import time
import clinic_api
from clinic_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clinic_api.ClientApi()
body = clinic_api.ClientIn() # ClientIn | 

try:
    # Create
    api_response = api_instance.client_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->client_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClientIn**](ClientIn.md)|  | 

### Return type

[**ClientOut**](ClientOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_delete**
> object client_delete(client_id)

Delete

### Example
```python
from __future__ import print_function
import time
import clinic_api
from clinic_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clinic_api.ClientApi()
client_id = NULL # object | 

try:
    # Delete
    api_response = api_instance.client_delete(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->client_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_get_all**
> object client_get_all()

Get All

### Example
```python
from __future__ import print_function
import time
import clinic_api
from clinic_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clinic_api.ClientApi()

try:
    # Get All
    api_response = api_instance.client_get_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->client_get_all: %s\n" % e)
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

# **client_get_by_id**
> ClientOut client_get_by_id(client_id)

Get By Id

### Example
```python
from __future__ import print_function
import time
import clinic_api
from clinic_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clinic_api.ClientApi()
client_id = NULL # object | 

try:
    # Get By Id
    api_response = api_instance.client_get_by_id(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->client_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | [**object**](.md)|  | 

### Return type

[**ClientOut**](ClientOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_update**
> ClientOut client_update(body)

Update

### Example
```python
from __future__ import print_function
import time
import clinic_api
from clinic_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clinic_api.ClientApi()
body = clinic_api.ClientUpdate() # ClientUpdate | 

try:
    # Update
    api_response = api_instance.client_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->client_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClientUpdate**](ClientUpdate.md)|  | 

### Return type

[**ClientOut**](ClientOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

