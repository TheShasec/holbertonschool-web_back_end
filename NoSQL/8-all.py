#!/usr/bin/env python3
"""434
s
f
sdf
s
fdsafddasfds
fsdfsdajfkdfjkdsfjlsf
saf
jdfklasjfsdjflsjfjsklfkdlfsfjSf
sal'fjsjfalkjflldfslfjslkfldfjjdf
f
fsjlsdflsdljsdlflfdjslajkdlaj"""


import pymongo


def list_all(mongo_collection):
    """
     Lists all documents in a collection
        Args:
            mongo_collection: Collection of object

        Return:
            List with documents, otherwise []
    """
    
    return list(mongo_collection.find())
