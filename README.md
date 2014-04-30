# Django Twitter Bootstrap Form

Render Django forms using the HTML described by the [Bootstrap 3](http://getbootstrap.com/css/#forms).

## Demo

A basic demo is availaible on this [sandbox](http://django-sandbox.geelweb.org/twitter-bootstrap-form)

## Installation

From PyPI

    pip install django-twitterbootstrap-form

From Source:

	python setup.py install

### About Bootstrap 2

You can install the 0.2 version of this lib if you still work with old versions
of [Twitter Bootstrap](http://twitter.github.com/bootstrap/base-css.html#forms)

From PyPI

    pip install django-twitterbootstrap-form==0.2

From Source:

    git checkout 0.2
    python setup.py install

## Requirements

 * Django>=1.4
 * django-widget-tweaks==1.3

## Configuration

### settings.py

Edit your settings.py file and add the following line into your INSTALLED_APPS

    'geelweb.django.twitter_bootstrap_form'

### HTML templates

Load the filters and use them

    {% load twitter_bootstrap %}

Default form

    <form role="form">
        {{ default_form|twitter_bootstrap }}
        <button type="submit" class="btn btn-default">Submit</button>
    </form>

Search form / Navbar form

    <form role="search" class="navbar-form">
        {{ search_form|twitter_bootstrap:"search" }}
        <button type="submit" class="btn btn-default">Search</button>
    </form>

Inline form

    <form role="form" class="form-inline">
        {{ inline_form|twitter_bootstrap:"inline" }}
        <button type="submit" class="btn btn-default">Sign in</button>
    </form>

Horizontal form

    <form role="form" class="form-horizontal">
        {{ horizontal_form|twitter_bootstrap:"horizontal" }}
        <div class="form-group">
            <div class="col-sm-offset-2 col-sm-10">
                <button type="submit" class="btn btn-default">Sign in</button>
            </div>
        </div>
    </form>


