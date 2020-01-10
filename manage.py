from flask_script import Manager
from rebel_explorer import create_app
from rebel_explorer.models import db
from flask_migrate import Migrate, MigrateCommand

app = create_app()
manager = Manager(app)

# db migrate
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

if __name__ == '__main__':
    manager.run()
