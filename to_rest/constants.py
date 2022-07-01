#options
LIST_METHOD = "LIST_METHOD"
RETREIVE_METHOD = "RETREIVE_METHOD"
CREATE_METHOD = "CREATE_METHOD"
UPDATE_METHOD = "UPDATE_METHOD"
PARTIAL_UPDATE_METHOD = "PARTIAL_UPDATE_METHOD"
DESTROY_METHOD = "DESTROY_METHOD"
GET_OBJECT_METHOD = "GET_OBJECT_METHOD"
GET_QUERYSET_METHOD = "GET_QUERYSET_METHOD"
CUSTOM_VIEW_PARAMS = "CUSTOM_VIEW_PARAMS"
EXCLUDE_FIELDS = "EXCLUDE_FIELDS"
SEARCH_FIELDS = "SEARCH_FIELDS"
METHOD_FIELDS = "METHOD_FIELDS"
CUSTOM_SERIALIZER = "CUSTOM_SERIALIZER"
DEFAULT_SERIALIZER = "DEFAULT_SERIALIZER"
VIEW_SET_ATTRIBUTES = "VIEW_SET_ATTRIBUTES"
REQUIRED_REVERSE_REL_FIELDS = "REQUIRED_REVERSE_REL_FIELDS"
DEFAULT_ACTIONS = "DEFAULT_ACTIONS"
CUSTOM_ACTIONS = "CUSTOM_ACTIONS"
DEFAULT_VIEW_SET = "DEFAULT_VIEW_SET"

#affixes
ONE_TO_MANY_LIST_ACTION = "oneToManyList_"
MANY_TO_MANY_LIST_ACTION = "manyToManyList_"
MANY_TO_MANY_DETAIL_ACTION = "manyToManyDetail_"
PROJECT_NAME_PREFIX = "DjangoToRest_"

#header keys
CONTENT_MESSAGE = "Content-Message"


#messages
NOT_A_MODEL_CLASS_MSG = "The decorated class must be a sub class django.db.models.Model"
NO_OBJECT_EXISTS = "No {} object exists"