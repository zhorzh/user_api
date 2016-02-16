from core.services import postgres
from identity.models.user import User

postgres.drop_all()
postgres.create_all()
