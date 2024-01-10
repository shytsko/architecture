# coding: utf-8

"""
    Clinic Service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PetIn(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'client_id': 'object',
        'name': 'object',
        'birthday': 'object'
    }

    attribute_map = {
        'client_id': 'client_id',
        'name': 'name',
        'birthday': 'birthday'
    }

    def __init__(self, client_id=None, name=None, birthday=None):  # noqa: E501
        """PetIn - a model defined in Swagger"""  # noqa: E501
        self._client_id = None
        self._name = None
        self._birthday = None
        self.discriminator = None
        self.client_id = client_id
        self.name = name
        self.birthday = birthday

    @property
    def client_id(self):
        """Gets the client_id of this PetIn.  # noqa: E501


        :return: The client_id of this PetIn.  # noqa: E501
        :rtype: object
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this PetIn.


        :param client_id: The client_id of this PetIn.  # noqa: E501
        :type: object
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def name(self):
        """Gets the name of this PetIn.  # noqa: E501


        :return: The name of this PetIn.  # noqa: E501
        :rtype: object
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PetIn.


        :param name: The name of this PetIn.  # noqa: E501
        :type: object
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def birthday(self):
        """Gets the birthday of this PetIn.  # noqa: E501


        :return: The birthday of this PetIn.  # noqa: E501
        :rtype: object
        """
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        """Sets the birthday of this PetIn.


        :param birthday: The birthday of this PetIn.  # noqa: E501
        :type: object
        """
        if birthday is None:
            raise ValueError("Invalid value for `birthday`, must not be `None`")  # noqa: E501

        self._birthday = birthday

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PetIn, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PetIn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
