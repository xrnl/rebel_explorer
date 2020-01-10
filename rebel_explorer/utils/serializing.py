"""helper functions for serialization of data"""


def dump_datetime(datetime_obj):
    """convert datetime object to string format"""
    if datetime_obj is None:
        return None
    return datetime_obj.strftime("%Y-%m-%dT%H:%M:%SZ")
