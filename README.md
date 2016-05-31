# Django template snippets for PyCharm

PyCharm supports auto-expanding certain keywords in Django templates to the corresponding Django template tag. PyCharm calls these live templates, other programs call them snippets. By default, only a handful of template tags are supported. This repo reflects my efforts of creating the remaining ones as I need them.

## How to use

Download `Django.xml` from this repo and put it in the templates directory of your [preferences directory](https://www.jetbrains.com/help/pycharm/2016.1/directories-used-by-pycharm-to-store-settings-caches-plugins-and-logs.html), e.g. on OS X `~/Library/Preferences/<PRODUCT><VERSION>/templates/Django.xml`.

Use them in django templates like so:

![Screencast](https://github.com/chlab/pycharm-django-live-templates/raw/master/screencast.gif)

## Contribute

Missing tags?
Define them in PyCharm *Settings > Editor > Live Templates > Django*. Look at the other tags to see how to define them.
Please send a pull request and I'll be happy to merge it!