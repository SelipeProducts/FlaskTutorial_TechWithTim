#makes website folder into a package
#can import folder to run files


from flask import Flask

def create_app():
  #__name__ is the name of the file that will be ran
  app = Flask(__name__)

  #Str that acts as key to encrypt session and cookies data
  app.config['SECRET_KEY'] = '1QAZ2WSX 3EDC4RFV'

  return app



