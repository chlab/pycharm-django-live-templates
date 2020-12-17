# Django template snippets for PyCharm

PyCharm supports auto-expanding certain keywords in Django templates to the corresponding Django template tag. PyCharm calls these live templates, other programs call them snippets. By default, only a handful of template tags are supported. This repo reflects my efforts of creating the remaining ones as I need them.

## Installation

### For Os X and Windows
Clone the repository and copy the `Django.xml` file copy it in the templates directory of your
[preferences directory](https://www.jetbrains.com/help/pycharm/directories-used-by-the-ide-to-store-settings-caches-plugins-and-logs.html#config-directory), e.g. on OS X `~/Library/Preferences/<PRODUCT><VERSION>/templates/Django.xml`.

### For Linux

~~~vim
git clone https://github.com/Daniel1404/pycharm-django-live-templates.git
cd pycharm-django-live-templates
./install.py
~~~

It will let you a prompt, where you choice the IDE folder. Then the **install.py** script will copy
the Django.xml file into the templates directory.

## How to use

Use them in django templates like so:

![Screencast](https://github.com/chlab/pycharm-django-live-templates/raw/master/screencast.gif)

## Contribute

Missing [tags](https://docs.djangoproject.com/en/1.9/ref/templates/builtins/)?
Define them in PyCharm *Settings > Editor > Live Templates > Django*. Look at the other tags to see how to define them.
Please send a pull request and I'll be happy to merge it!
