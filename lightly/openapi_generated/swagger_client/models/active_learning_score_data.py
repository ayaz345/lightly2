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


from typing import List, Union
from pydantic import Extra,  BaseModel, Field, StrictFloat, StrictInt, conint, conlist, constr, validator

class ActiveLearningScoreData(BaseModel):
    """
    ActiveLearningScoreData
    """
    id: constr(strict=True) = Field(..., description="MongoDB ObjectId")
    tag_id: constr(strict=True) = Field(..., alias="tagId", description="MongoDB ObjectId")
    score_type: constr(strict=True, min_length=1) = Field(..., alias="scoreType", description="Type of active learning score")
    scores: conlist(Union[StrictFloat, StrictInt], min_items=1) = Field(..., description="Array of active learning scores")
    created_at: conint(strict=True, ge=0) = Field(..., alias="createdAt", description="unix timestamp in milliseconds")
    __properties = ["id", "tagId", "scoreType", "scores", "createdAt"]

    @validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-f0-9]{24}$", value):
            raise ValueError(r"must validate the regular expression /^[a-f0-9]{24}$/")
        return value

    @validator('tag_id')
    def tag_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-f0-9]{24}$", value):
            raise ValueError(r"must validate the regular expression /^[a-f0-9]{24}$/")
        return value

    @validator('score_type')
    def score_type_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9_+=,.@:\/-]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9_+=,.@:\/-]*$/")
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
    def from_json(cls, json_str: str) -> ActiveLearningScoreData:
        """Create an instance of ActiveLearningScoreData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self, by_alias: bool = False):
        """Returns the dictionary representation of the model"""
        return self.dict(by_alias=by_alias, exclude={}, exclude_none=True)

    @classmethod
    def from_dict(cls, obj: dict) -> ActiveLearningScoreData:
        """Create an instance of ActiveLearningScoreData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ActiveLearningScoreData.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj:
            if _key not in cls.__properties:
                raise ValueError(
                    f"Error due to additional fields (not defined in ActiveLearningScoreData) in the input: {obj}"
                )

        return ActiveLearningScoreData.parse_obj(
            {
                "id": obj.get("id"),
                "tag_id": obj.get("tagId"),
                "score_type": obj.get("scoreType"),
                "scores": obj.get("scores"),
                "created_at": obj.get("createdAt"),
            }
        )

