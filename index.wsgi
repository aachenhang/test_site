from bottle import Bottle, run, template, route

#import sae

app = Bottle()

@app.route('/')
def hello():
	return template('index')
    # return "Hello, world! - Chenhang123"

#@app.get('/')

#run in sina sae
#application = sae.create_wsgi_app(app)

#run in own PC
run(app=app, host='0.0.0.0', port=80, debug=True)
