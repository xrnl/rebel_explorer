import json

from ._db import db


class LocalGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False, unique=True)

    # one to many relationship with members
    members = db.relationship('Member', back_populates='local_group')

    def __repr__(self):
        return f"LocalGroup({self.name})"

    def get_members_serialized(self):
        return [m.serialize for m in self.members]

