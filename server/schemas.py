

from config import ma
from models import User

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True
        fields = ('id', 'name', 'email', 'is_admin', 'two_factor_enabled', 'hubspot_contact_id')

user_schema = UserSchema()
users_schema = UserSchema(many=True)