""" Another way to run the app"""

from src import create_app
from src import db

db.create_all()

app = create_app()

if __name__ == "__main__":
    app.run()

