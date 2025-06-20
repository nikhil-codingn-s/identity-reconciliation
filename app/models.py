from .database import db
from datetime import datetime

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phoneNumber = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    linkedId = db.Column(db.Integer, nullable=True)  # Points to primary contact ID
    linkPrecedence = db.Column(db.String(10), nullable=False)  # 'primary' or 'secondary'
    createdAt = db.Column(db.DateTime, default=datetime.utcnow)
    updatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deletedAt = db.Column(db.DateTime, nullable=True)
