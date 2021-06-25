
from flask import Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.models import Configuration, User
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, ConfigurationAlreadyExistsError, InternalServerError, UpdatingConfigurationError, DeletingConfigurationError, ConfigurationNotExistsError
# pylint: disable=no-member
# pylint: disable=unused-variable
import json
import os



class ConfigurationsApi(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        
        configurations = Configuration.objects().filter(added_by=user_id).to_json()

        response= Response(configurations, mimetype="application/json", status=200)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS, HEAD'
        response.headers['Access-Control-Max-Age'] = '1209600'
        return response
    @jwt_required()
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
    @jwt_required()
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
    
    @jwt_required()
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

class RunCommands(Resource):
    @jwt_required()
    def post(self):
        try:
            # os.system('cmd /c "cd C:\\Users\\marti\\Downloads & kubectl apply -f hello-deploy.yaml & kubectl apply -f hello-service.yaml "')
            body = request.get_json()
            command='cmd /c "cd C:\\Users\\marti\\Downloads'
            for x in body:
                print(x)
                command+=' & kubectl apply -f '+x+'.yaml'
            command+='"'
            print(command)
            os.system(command)
        except Exception:
            raise InternalServerError