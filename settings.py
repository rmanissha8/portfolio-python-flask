from dotenv import load_dotenv

import os

load_dotenv()


FLASK_ENV=os.getenv("FLASK_ENV")
FLASK_APP=os.getenv("FLASK_APP")
FLASK_RUN_PORT=os.getenv("FLASK_RUN_PORT")