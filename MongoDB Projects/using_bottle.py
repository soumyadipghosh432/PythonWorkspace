from bottle import route, run, template

@route('/bottleApp/<name>')

def index(name):
    return template('<strong>Hello {{x_var}} ! Welcome to page.', x_var=name)

#  this will run the program as a listener to HTTP connections
run(host='localhost', port=8088)
