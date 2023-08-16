#!/usr/bin/env python3
""" Mongodb Update """


def update_topics(mongo_collection, name, topics):
    """Update the doc by name """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
