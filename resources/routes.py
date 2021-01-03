from .configuration import ConfigurationsApi, ConfigurationApi
from .auth import SignupApi, LoginApi

def initialize_routes(api):
    api.add_resource(ConfigurationsApi, '/api/configurations')
    api.add_resource(ConfigurationApi, '/api/configurations/<id>')

    api.add_resource(SignupApi,'/api/auth/signup')
    api.add_resource(LoginApi,'/api/auth/login')
    