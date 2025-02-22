# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@lightly.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import Extra,  BaseModel, Field, StrictStr, conlist
from lightly.openapi_generated.swagger_client.models.configuration_entry import ConfigurationEntry

class ConfigurationSetRequest(BaseModel):
    """
    ConfigurationSetRequest
    """
    name: StrictStr = Field(...)
    configs: conlist(ConfigurationEntry) = Field(...)
    __properties = ["name", "configs"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True
        use_enum_values = True
        extra = Extra.forbid

    def to_str(self, by_alias: bool = False) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.dict(by_alias=by_alias))

    def to_json(self, by_alias: bool = False) -> str:
        """Returns the JSON representation of the model"""
        return json.dumps(self.to_dict(by_alias=by_alias))

    @classmethod
    def from_json(cls, json_str: str) -> ConfigurationSetRequest:
        """Create an instance of ConfigurationSetRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self, by_alias: bool = False):
        """Returns the dictionary representation of the model"""
        _dict = self.dict(by_alias=by_alias,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in configs (list)
        _items = []
        if self.configs:
            _items.extend(
                _item.to_dict(by_alias=by_alias) for _item in self.configs if _item
            )
            _dict['configs' if by_alias else 'configs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConfigurationSetRequest:
        """Create an instance of ConfigurationSetRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConfigurationSetRequest.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj:
            if _key not in cls.__properties:
                raise ValueError(
                    f"Error due to additional fields (not defined in ConfigurationSetRequest) in the input: {obj}"
                )

        return ConfigurationSetRequest.parse_obj(
            {
                "name": obj.get("name"),
                "configs": [
                    ConfigurationEntry.from_dict(_item)
                    for _item in obj.get("configs")
                ]
                if obj.get("configs") is not None
                else None,
            }
        )

