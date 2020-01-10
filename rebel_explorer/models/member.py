from datetime import datetime
from ._db import db
from rebel_explorer.utils.serializing import dump_datetime
from sqlalchemy import Integer, ForeignKey

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    name = db.Column(db.Text)
    surname = db.Column(db.Text)
    phone = db.Column(db.Text)
    created_date = db.Column(db.DateTime, nullable=False)
    modified_date = db.Column(db.DateTime, nullable=False)
    added_date = db.Column(db.DateTime, default=datetime.utcnow())

    # many to one relationship with local group
    local_group_id = db.Column(Integer, ForeignKey('local_group.id'))
    local_group = db.relationship('LocalGroup', back_populates='members')

    def __repr__(self):
        return f"Member({self.email})"

    def local_group_name(self):
        return self.local_group.name

    @property
    def serialize(self):
        """Return object data in a format easily serializable to json"""
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'phone': self.phone,
            'local_group': self.local_group_name(),
            'created_date': dump_datetime(self.created_date)
        }
