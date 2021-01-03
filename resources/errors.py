class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class ConfigurationAlreadyExistsError(Exception):
    pass

class UpdatingConfigurationError(Exception):
    pass

class DeletingConfigurationError(Exception):
    pass

class ConfigurationNotExistsError(Exception):
    pass

class EmailAlreadyExistsError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "ConfigurationAlreadyExistsError": {
        "message": "Configuration with given name already exists",
        "status": 400
    },
    "UpdatingConfigurationError": {
        "message": "Updating configuration added by other is forbidden",
        "status": 403
    },
    "DeletingConfigurationError": {
        "message": "Deleting configuration added by other is forbidden",
        "status": 403
    },
    "ConfigurationNotExistsError": {
        "message": "Configuration with given id doesn't exists",
        "status": 400
    },
    "EmailAlreadyExistsError": {
        "message": "User with given email address already exists",
        "status": 400
    },
    "UnauthorizedError": {
        "message": "Invalid username or password",
        "status": 401
    }
}