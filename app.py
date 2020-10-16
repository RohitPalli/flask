from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_cloud():
   f = open('README.md', 'r')
   file_contents = f.read()
   print (file_contents)
   f.close()
   return ' This is a static Web page with Python Flask Web Framework in Google Cloud Platform using Terraform Orchestration tool'

app.run(host='0.0.0.0')
