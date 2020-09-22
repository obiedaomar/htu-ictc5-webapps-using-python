from ..core.database import db

class TaskList(db.Document):
    name = db.StringField()
    description = db.StringField()
    owner_id = db.StringField()
    is_public= db.BoolField(default =False)
    search_keyword = db.StringField()
