#!/usr/bin/env python3
"""32423423
4234fdasdfaasfaf
sdaffjiidfuisdfdfjidf
asfadsjfdsfdfjdjf
sfjlsfsadjfka"""


import pymongo


def schools_by_topic(mongo_collection, topic):
    """fdkfjsdaf
    dsfadsfasdflsdfsdfsdfsd
    fsdfsadfjkdfsdfjdsfjkffjkd
    fsjfkajfdafjlkdl"""

    return list(mongo_collection.find({"topic":topic}))
