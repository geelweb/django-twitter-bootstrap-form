# Django Twitter Bootstrap Form

Render Django forms using the HTML described by the [Twitter Bootstrap](http://twitter.github.com/bootstrap/base-css.html#forms)

## Installation

From Source:

    python setup.py build
	sudo python setup.py install

## Configuration

### settings.py

Edit your settings.py file and add the following line into your INSTALLED_APPS

    'geelweb.django.twitter_bootstrap_form'

### HTML templates

Load the filters and use them

    {% load twitter_bootstrap %}

Default form

    <form>
        <fieldset>
            <legend>Legend</legend>
            {{ form|twitter_bootstrap }}
            <button type="submit" class="btn">Submit</button>
        </fieldset>
    </form>

Search form

    <form class="form-search">
        {{ form|twitter_bootstrap:"search" }}
        <button type="submit" class="btn">Search</button>
    </form>

Inline form

    <form class="form-inline">
        {{ form|twitter_bootstrap:"inline" }}
        <button type="submit" class="btn">Sign in</button>
    </form>

