import sqlite3
import click
from flask import current_app, g

def fetch_db():
    if 'db' not in g:
        g.db =sqlite3.connect(current_app.config['DATABASE'],
                              detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
        return g.db

def close(e = None):
    db = g.pop('db', None)
    
    if db is not None:
        db.close()

def init():
    db=fetch_db()
    
    with current_app.open_resource('schema.sql') as schema:
        db.executescript(schema.read().decode('utf8'))
        
        
#custom command line command. chech https://flask.palletsprojects.com/en/2.2.x/cli/
@click.command('init-db')
def init_db_command():
     """Clear the existing data and create new tables."""
     init()
     click.echo('Initialized the database.')
     
def init_app(app):
    app.teardown_appcontext(close)
    app.cli.add_command(init_db_command)