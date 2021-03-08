from website import create_app
import random

app = create_app()

#security**
#only if we run this file not import the file
#without line 8: we can import main.py from other file and start the webserver.
if __name__ == '__main__':
  #app.run starts application
  #app.run(debug=True)#single-line run and debug does not work on repl.it
  #debug == true reruns server when change is made to code
  app.debug = True
  app.run(host='0.0.0.0',
  port=random.randint(2000, 9000))
  


