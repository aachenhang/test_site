from bottle import Bottle, run, template, route, static_file

#import sae

app = Bottle()

@app.route('/')
def hello():
	return template('index')
    # return "Hello, world! - Chenhang123"








@app.route('/bootstrap/css/<filename>')
def server_static(filename):
    return static_file(filename, root='./bootstrap/css/')

@app.route('/bootstrap/font/<filename>')
def server_static(filename):
    return static_file(filename, root='./bootstrap/font/')

@app.route('/bootstrap/js/<filename>')
def server_static(filename):
    return static_file(filename, root='./bootstrap/js/')

@app.route('/css/<filename>')
def server_static(filename):
    return static_file(filename, root='./css/')

@app.route('/fonts/font-awesome/css/<filename>')
def server_static(filename):
    return static_file(filename, root='./fonts/font-awesome/css/')

@app.route('/fonts/font-awesome/fonts/<filename>')
def server_static(filename):
    return static_file(filename, root='./fonts/font-awesome/fonts/')

@app.route('/fonts/font-awesome/less/<filename>')
def server_static(filename):
    return static_file(filename, root='./fonts/font-awesome/less/')

@app.route('/fonts/font-awesome/scss/<filename>')
def server_static(filename):
    return static_file(filename, root='./fonts/font-awesome/scss/')

@app.route('/images/<filename>')
def server_static(filename):
    return static_file(filename, root='./images/')

@app.route('/js/<filename>')
def server_static(filename):
    return static_file(filename, root='./js/')

@app.route('/plugins/isotope/<filename>')
def server_static(filename):
    return static_file(filename, root='./plugins/isotope/')

@app.route('/plugins/<filename>')
def server_static(filename):
    return static_file(filename, root='./plugins/')
#run in sina sae
#application = sae.create_wsgi_app(app)

#run in own PC
run(app=app, host='localhost', port=8080, debug=True)
