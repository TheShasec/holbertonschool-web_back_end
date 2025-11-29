#!/usr/bin/env python3
"""434"""


import pymongo


def list_all(mongo_collection):
    """e343243"""
    
    return mongo_collection.find()
