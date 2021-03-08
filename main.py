from website import create_app

app = create_app()

#security**
#only if we run this file not import the file
#without line 8: we can import main.py from other file and start the webserver.
if __name__ == '__main__':
  #app.run starts application
  app.run(debug=True)
  #debug == true reruns server when change is made to code


