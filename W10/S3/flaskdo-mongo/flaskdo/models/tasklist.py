from ..core.database import db

class TaskList(db.Document):
    name = db.StringField()
    description = db.StringField()