from flask import render_template, redirect

from app import app, pages

# Helper functions
def get_news():
    news = [p for p in pages if 'tags' in p.meta and 'news' in p['tags']]
    latest = sorted(news, reverse=True, key=lambda p: p.meta['date'])

    return latest

def get_sidebar():
    """
    This function returns all the nessessary data for using the sidebar.
    """

    # get all news
    latest = get_news()

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


    return sorted(acm, key=lambda k: k.meta['order']), sorted(acmw, key=lambda k: k.meta['order'])

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

@app.route('/resumedrop')
def resumedrop():
	url = "https://script.google.com/macros/s/AKfycbyWsq2FbgY3eWc0qrTEY4a2vZGJ8mrGHP_fbJCUebmV3uEQPg/exec"
	return redirect(url, code=302)

# Custom Jinja filters
def nowhitespace(value):    # currently not in use
    return str(value).replace(' ', '')
