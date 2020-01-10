# Will implement later

from datetime import datetime
from app import db
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(150), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return '<Item %r>' % self.id