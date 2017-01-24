# ACM-Site

This website is built using Flask framework and associated libraries.

## Contents

### Pages

The pages directory contains .md files which are used to dynamically generate
pages using the Flask-FlatPages library. Dynamic pages are rendered using
the `page.html` template without the inner content block.

### Static

This directory contains static files such as image assets, Javascript files,
and CSS stylesheets. Please consult Flask's `url_for` function to access these
files.

### Templates

This directory has Jinja2 HTML templates which are dynamically populated by
the flask `render_template` function, sometimes in conjunction with Flask-FlatPages.
