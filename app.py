from flask import Flask
from datetime import datetime
import pybrake.flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PYBRAKE'] = dict(
    project_id=237813,
    project_key='3ee9d6fc6b462f0dae3b37a41366e914'

# export AIRBRAKE_API_KEY=
# export AIRBRAKE_PROJECT_ID=
# export AIRBRAKE_ENVIRONMENT=production


)
app = pybrake.flask.init_app(app)


# init db session for the whole app
db = SQLAlchemy(app)
# do something with app...

if __name__ == "__main__":
    app.run(debug=True)

# import airbrake

# logger = airbrake.getLogger(api_key="3ee9d6fc6b462f0dae3b37a41366e914", project_id=237813)

# try:
#     1/0
# except Exception:
#     logger.exception("Bad math.")

