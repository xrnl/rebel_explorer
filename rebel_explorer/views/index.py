from flask import render_template
from flask.blueprints import Blueprint
from sqlalchemy.orm.exc import NoResultFound
from flask import abort

from rebel_explorer.models import LocalGroup

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/<local_group_name>')
def local_group(local_group_name):
    try:
        local_group = LocalGroup.query.filter(LocalGroup.name.ilike(local_group_name)).one()
    except NoResultFound:
        abort(404)

    return render_template('local_group.html',
                           local_group=local_group_name,
                           members=local_group.get_members_serialized())
