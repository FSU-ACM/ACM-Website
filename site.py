#!/usr/bin/env python

from flask import Flask, render_template, request
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
app.url_map.strict_slashes = False


# Nav
topbar = Navbar('ACM at FSU',
    Link('Home', '/'),
    Link('About', '/about'),
    Link('Sponsors', '#'),
    Link('Contest', '#'),
    Subgroup('Links',
        Link('Slack', '#'),
        Link('Facebook', '#'),
        Link('Nole Central', '#'),
    )
)

nav = Nav()
nav.register_element('top', topbar)
nav.init_app(app)

# Helper functions
def get_sidebar():
    """
    This function returns all the nessessary data for using the sidebar.
    """

    # get all news
    news = [p for p in pages if 'tags' in p.meta and 'news' in p['tags']]
    latest = sorted(news, reverse=True, key=lambda p: p.meta['date'])

    # get all tags CURRENTLY DOESN"T WORK (optimize pls)
    tags = set()
    for p in pages:
        if 'tags' in p.meta:
            tags.union(set(p['tags']))

    return latest, list(tags)


# Routes
@app.route('/')
def index():
    latest, tags = get_sidebar()
    return render_template('page.html',
        isindex = True,
        latest=latest,
        tags=tags)

@app.route('/<path:path>/')
def page(path):
    latest, tags = get_sidebar()
    return render_template('page.html',
        isindex = False,
        page = pages.get_or_404(path),
        latest=latest,
        tags=tags)

# Custom Jinja filters
def nowhitespace(value):    # currently not in use
    return str(value).replace(' ', '')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
