#makes website folder into a package
#can import folder to run files


from flask import Flask

def create_app():
  #__name__ is the name of the file that will be ran
  app = Flask(__name__)

  #Str that acts as key to encrypt session and cookies data
  app.config['SECRET_KEY'] = '1QAZ2WSX 3EDC4RFV'

  #telling flask where to find routes
  from .views import views
  from .auth import auth

  #register routes
  #prefixes add sub url    .../suburl/index
  app.register_blueprint(views, url_prefix = '/')
  app.register_blueprint(auth, url_prefix = '/')
  return app



