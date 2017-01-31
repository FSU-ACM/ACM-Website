from flask import Flask
from flask_flatpages import FlatPages
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *

# Init
app = Flask(__name__)
pages = FlatPages(app)
bootstrap = Bootstrap(app)


# Config
app.config['FLATPAGES_AUTO_RELOAD'] = True
app.config['FLATPAGES_EXTENSION'] = '.md'
app.config['FREEZER_RELATIVE_URLS'] = True
# app.config['FREEZER_DEFAULT_MIMETYPE'] = 'text/html; charset=utf-8'
app.url_map.strict_slashes = False


# Nav
topbar = Navbar('ACM at FSU',
	Link('Home', '/'),
	Link('About', '/about'),
	Link('Sponsors', '/sponsors'),
	Link('Contest', 'http://springprogrammingcontest.com'),
	Subgroup('Links',
		Link('Slack', 'https://acmatfsu.slack.com'),
		Link('Facebook', 'https://www.facebook.com/groups/cs.fsu.acm/'),
		Link('Nole Central', 'https://nolecentral.dsa.fsu.edu/organization/associationforcomputingmachinery'),
		Link('Resume Drop', 'https://script.google.com/macros/s/AKfycbyWsq2FbgY3eWc0qrTEY4a2vZGJ8mrGHP_fbJCUebmV3uEQPg/exec'),
	)
)

nav = Nav()
nav.register_element('top', topbar)
nav.init_app(app)

from views import *
