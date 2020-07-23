class ObjectDoesNotExists(Exception):
    pass

def get_count_field_from_object(database_handler, object_id):
    
    try:
        obj = database_handler.get(id=object_id)
    except Exception:
        raise ObjectDoesNotExists
    
    return obj.id