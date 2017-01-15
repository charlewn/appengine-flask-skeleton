"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask

# import your classes
from handlers import page
from handlers.admin import admin

app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


#for most pages
app.add_url_rule(r'/support', view_func=page.Support.as_view('support'))

app.add_url_rule(r'/', view_func=page.Index.as_view('index'))

#for admin pages
app.add_url_rule(r'/admin', view_func=admin.AdminPage.as_view('admin_page'))



@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
