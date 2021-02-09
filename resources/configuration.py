
from flask import Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.models import Configuration, User
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, ConfigurationAlreadyExistsError, InternalServerError, UpdatingConfigurationError, DeletingConfigurationError, ConfigurationNotExistsError

class ConfigurationsApi(Resource):
    def get(self):
        configurations = Configuration.objects().to_json()
        return Response(configurations, mimetype="application/json", status=200)
    #@jwt_required
    def post(self):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            user = User.objects.get(id=user_id)
            configuration = Configuration(**body, added_by=user)
            configuration.save()
            user.update(push__configurations=configuration)
            user.save()
            id = configuration.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise ConfigurationAlreadyExistsError
        except Exception as e:
            raise InternalServerError
    
class ConfigurationApi(Resource):
    @jwt_required
    def put(self, id):
        try:
            user_id = get_jwt_identity()
            configuration = Configuration.objects.get(id=id, added_by=user_id)
            body = request.get_json()
            Configuration.objects.get(id=id).update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingConfigurationError
        except Exception:
            raise InternalServerError 
    
    @jwt_required
    def delete(self, id):
        try:
            user_id=get_jwt_identity()
            configuration = Configuration.objects.get(id=id,added_by=user_id)
            configuration.delete()
            return '', 200
        except DoesNotExist:
            raise DeletingConfigurationError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            configurations = Configuration.objects.get(id=id).to_json()
            return Response(configurations, mimetype="application/json", status=200)
        except DoesNotExist:
            raise ConfigurationNotExistsError
        except Exception:
            raise InternalServerError
