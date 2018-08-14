import bottle

""" ====================================================================
    Below set of example shows direct way of defining routing.
    This will set the route with the definition of functions.
==================================================================== """    

""" Create an object of Bottle to enable the use of web framework """
webApp = bottle.Bottle()

""" Set response to routed URL navigation """
@webApp.route('/hello')
def showMsg():
    return "Hello Guest !"


@webApp.route('/welcome')
def showMsg():
    return "Welcome Guest !"


""" We can use common function to serve for multiple navigation route """
@webApp.route('/')
@webApp.route('/greet')
@webApp.route('/greet/<user>')
def showMsg(user="Guest"):
    return "Good Morning " + user + "!"


webApp.run(host='localhost', port=8899)



""" ====================================================================
    Below set of example shows explicit way of routing configuration.
    Here we setup methods to configure and define them seperately
==================================================================== """    

def setup_routing(webApp):
    webApp.route('/', 'GET', index)
    webApp.route('/welcome', ['GET', 'POST'], welcome)
    webApp.route('/welcome/<name>', ['GET', 'POST'], welcome)


def index():
    return "Good Morning Guest !"

def welcome(name="Guest"):
    return "Welcome " + name + " !"


webApp = bottle.Bottle()
setup_routing(webApp)
webApp.run(host='localhost', port=8899)
