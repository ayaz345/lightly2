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



from pydantic import Extra,  BaseModel, Field, constr, validator
from lightly.openapi_generated.swagger_client.models.datasource_config_base import DatasourceConfigBase

class DatasourceConfigOBS(DatasourceConfigBase):
    """
    DatasourceConfigOBS
    """
    obs_endpoint: constr(strict=True, min_length=1) = Field(..., alias="obsEndpoint", description="The Object Storage Service (OBS) endpoint to use of your S3 compatible cloud storage provider")
    obs_access_key_id: constr(strict=True, min_length=1) = Field(..., alias="obsAccessKeyId", description="The Access Key Id of the credential you are providing Lightly to use")
    obs_secret_access_key: constr(strict=True, min_length=1) = Field(..., alias="obsSecretAccessKey", description="The Secret Access Key of the credential you are providing Lightly to use")
    __properties = ["id", "purpose", "type", "fullPath", "thumbSuffix", "obsEndpoint", "obsAccessKeyId", "obsSecretAccessKey"]

    @validator('obs_endpoint')
    def obs_endpoint_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^https?:\/\/.+$", value):
            raise ValueError(r"must validate the regular expression /^https?:\/\/.+$/")
        return value

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
    def from_json(cls, json_str: str) -> DatasourceConfigOBS:
        """Create an instance of DatasourceConfigOBS from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self, by_alias: bool = False):
        """Returns the dictionary representation of the model"""
        return self.dict(by_alias=by_alias, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> DatasourceConfigOBS:
        """Create an instance of DatasourceConfigOBS from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DatasourceConfigOBS.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj:
            if _key not in cls.__properties:
                raise ValueError(
                    f"Error due to additional fields (not defined in DatasourceConfigOBS) in the input: {obj}"
                )

        return DatasourceConfigOBS.parse_obj(
            {
                "id": obj.get("id"),
                "purpose": obj.get("purpose"),
                "type": obj.get("type"),
                "full_path": obj.get("fullPath"),
                "thumb_suffix": obj.get("thumbSuffix"),
                "obs_endpoint": obj.get("obsEndpoint"),
                "obs_access_key_id": obj.get("obsAccessKeyId"),
                "obs_secret_access_key": obj.get("obsSecretAccessKey"),
            }
        )

