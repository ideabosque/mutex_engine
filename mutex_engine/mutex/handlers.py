#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from time import time
from pynamodb.exceptions import DoesNotExist
from mutex_engine.mutex.models import MutexModel

__author__ = "bl"

# ! expires_in : ms
def lock(identifier, expires_in=100):
    try:
        if not identifier:
            raise Exception("identifier is required")

        identifier = str(identifier).strip().lower()
        locked_at = int(round(time() * 1000))
        exists = True

        try:
            model = MutexModel.get(identifier)

            if model.expires_in + model.locked_at >= locked_at:
                return False

            # for model in MutexModel.query(identifier):
            #     exists = True

            #     if model.expires_in + model.locked_at >= locked_at:
            #         return False
        except DoesNotExist:
            exists = False
            pass

        if exists:
            actions = [
                MutexModel.locked_at.set(locked_at),
                MutexModel.expires_in.set(int(expires_in)),
            ]

            MutexModel(identifier).update(
                actions=actions,
                condition=(MutexModel.identifier == str(identifier).strip()),
            )
        else:
            MutexModel(
                identifier,
                **{
                    "locked_at": locked_at,
                    "expires_in": int(expires_in),
                },
            ).save()

        return True
    except Exception as e:
        raise e
