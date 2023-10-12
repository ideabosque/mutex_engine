#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute,
    NumberAttribute,
)
import os

# from pynamodb.indexes import GlobalSecondaryIndex, LocalSecondaryIndex, AllProjection

__author__ = "bl"


class BaseModel(Model):
    class Meta:
        billing_mode = "PAY_PER_REQUEST"
        region = os.getenv("REGIONNAME")


class MutexModel(BaseModel):
    class Meta(BaseModel.Meta):
        table_name = "se-locks"

    identifier = UnicodeAttribute(hash_key=True)
    locked_at = NumberAttribute(default=0)
    expires_in = NumberAttribute(default=0)
