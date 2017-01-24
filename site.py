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
    Link('Sponsors', '/sponsors'),
    Link('Contest', 'http://springprogrammingcontest.com'),
    Subgroup('Links',
        Link('Slack', 'https://acmatfsu.slack.com'),
        Link('Facebook', 'https://www.facebook.com/groups/cs.fsu.acm/'),
        Link('Nole Central', 'https://nolecentral.dsa.fsu.edu/organization/associationforcomputingmachinery'),
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

def get_officers():
    """
    This function returns a tuple of officers: ACM,ACM-W
    """

    # get all officers
    acm = [p for p in pages if 'org' in p.meta and p['org'] == 'ACM']
    acmw = [p for p in pages if 'org' in p.meta and p['org'] == 'ACM-W']


    return sorted(acm, key=lambda k: k.meta['order']), acmw #sorted(acmw, key=lambda k: k.meta['order'])

def get_sponsors():
    return None

# Routes
@app.route('/')
def index():
    latest, tags = get_sidebar()
    return render_template('index.html',
        latest=latest,
        tags=tags)

@app.route('/about')
def about():
    latest, tags = get_sidebar()
    acm, acmw = get_officers()
    return render_template('about.html',
        page=pages.get_or_404('about'),
        latest=latest,
        acm=acm,
        acmw=acmw)

@app.route('/sponsors')
def sponsors():
    latest, tags = get_sidebar()
    sponsors = get_sponsors()
    return render_template('sponsors.html',
        page=pages.get_or_404('sponsors'),
        latest=latest,
        sponsors=sponsors)

@app.route('/<path:path>/')
def page(path):
    latest, tags = get_sidebar()
    return render_template('page.html',
		dynamic_page=True,
        page=pages.get_or_404(path),
        latest=latest)

# Custom Jinja filters
def nowhitespace(value):    # currently not in use
    return str(value).replace(' ', '')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
