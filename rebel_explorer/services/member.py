from sqlalchemy.orm.exc import NoResultFound

from rebel_explorer.models import db, Member, LocalGroup
from rebel_explorer.utils.parsing import extract_member_data
from more_itertools import one
import re


def store_members(members):
    for m in members:
        m = extract_member_data(m)

        local_group = m['local_group']
        m.pop('local_group')
        member = Member(**m)

        if local_group:
            try:
                # cache results if function is too slow
                local_group = LocalGroup.query.filter_by(name=local_group).one()
            except NoResultFound:
                local_group = LocalGroup(name=local_group)

        member_existing = Member.query.filter_by(email=member.email).first()
        if member_existing:
            member.id = member_existing.id
            member_existing.local_group = local_group
            db.session.merge(member)
        else:
            member.local_group = local_group
            db.session.add(member)

    db.session.commit()
