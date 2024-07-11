from flask_restx import Namespace, Resource, fields

api = Namespace("auth", description="JWT")

authentication_input_fields = api.model(
    name="PasswordInput",
    model={
        "name":fields.String(description="Name of the amenity", min_length=2),
    },    
)

class Auth(Resource):
    pass