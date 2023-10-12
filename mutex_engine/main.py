#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from mutex_engine.mutex.handlers import lock

__author__ = "bl"


class Mutex(object):
    def __init__(self, logger, **setting):
        self.logger = logger
        self.setting = setting

    # Add new log
    def lock(self, identifier, expires_in=100):
        try:
            return lock(identifier=identifier, expires_in=expires_in)
        except Exception as e:
            raise e
