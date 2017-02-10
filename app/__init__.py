from flask import Flask, render_template_string
from flask_flatpages import FlatPages, pygmented_markdown
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
		Link('Resume Drop', '/resumedrop'),
	)
)

nav = Nav()
nav.register_element('top', topbar)
nav.init_app(app)

# Fix renderer for jinja and md
def prerender_jinja(text):
    prerendered_body = render_template_string(Markup(text))
    return pygmented_markdown(prerendered_body)

app.config['FLATPAGES_HTML_RENDERER'] = prerender_jinja


# Cache busting
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)



from views import *
