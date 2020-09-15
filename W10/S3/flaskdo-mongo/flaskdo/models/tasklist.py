from ..core.database import db

class TaskList(db.Document):
    name = db.StringField()
    description = db.StringField()
    owner_id = db.StringField()