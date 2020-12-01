from pyrebase import pyrebase
import json
from github import Github
from os import getenv

firebase_config = json.loads(Github(
    getenv("ACCESS_TOKEN")
).get_gist("37bbbbce6b64b2f4a5d3195d7d06df92").files["firebase_config.json"].content)

firebase = pyrebase.initialize_app(firebase_config)
database = firebase.database()
