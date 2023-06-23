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



from pydantic import Extra,  BaseModel, Field, constr
from lightly.openapi_generated.swagger_client.models.datasource_config_base import DatasourceConfigBase

class DatasourceConfigAzure(DatasourceConfigBase):
    """
    DatasourceConfigAzure
    """
    account_name: constr(strict=True, min_length=1) = Field(..., alias="accountName", description="name of the Azure Storage Account")
    account_key: constr(strict=True, min_length=1) = Field(..., alias="accountKey", description="key of the Azure Storage Account")
    __properties = ["id", "purpose", "type", "fullPath", "thumbSuffix", "accountName", "accountKey"]

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
    def from_json(cls, json_str: str) -> DatasourceConfigAzure:
        """Create an instance of DatasourceConfigAzure from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self, by_alias: bool = False):
        """Returns the dictionary representation of the model"""
        return self.dict(by_alias=by_alias, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> DatasourceConfigAzure:
        """Create an instance of DatasourceConfigAzure from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DatasourceConfigAzure.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj:
            if _key not in cls.__properties:
                raise ValueError(
                    f"Error due to additional fields (not defined in DatasourceConfigAzure) in the input: {obj}"
                )

        return DatasourceConfigAzure.parse_obj(
            {
                "id": obj.get("id"),
                "purpose": obj.get("purpose"),
                "type": obj.get("type"),
                "full_path": obj.get("fullPath"),
                "thumb_suffix": obj.get("thumbSuffix"),
                "account_name": obj.get("accountName"),
                "account_key": obj.get("accountKey"),
            }
        )

