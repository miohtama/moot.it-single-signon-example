Moot.it forum integration example with Django
-----------------------------------------------

Single-sign-on JavaScript embeddable forms for Django from `moot.it <http://moot.it>`_.

* Integrates with `django-avatar <https://pypi.python.org/pypi/django-avatar/>`_
  to set user forum avatar photos.

* `django-registration <hhttps://django-registration.readthedocs.org/en/latest/>`_ based user sign up
  workflow

* `django-registration-defaults <https://github.com/yourcelf/django-registration-defaults>`_ provides
  dummy log in and sign up form templates needed to test the example

Running
---------

Create Moot.it account and register to their single sign-on program (20 USD as writing of this).

**Note**: You can test the avatar image part without actually signing up to Moot.it. Just supply
a dummy API key. Avatar form works even if the forum doesn't load.

First get `virtualenv <https://pypi.python.org/pypi/virtualenv/>`_ to your OS.

Example (Python 2.7)::

    git clone git@github.com:miohtama/moot.it-single-signon-example.git
    cd moot.it-single-signon-example
    virtualenv venv  # Use virtualenv command for your Python
    source venv/bin/activate
    pip install Django==1.4  # Install django
    pip install Pillow==2.1.0 # Image handling
    pip install python-magic==0.4.3
    pip install django-registration==1.0 # User sign up
    pip install "git+https://github.com/yourcelf/django-registration-defaults.git#egg=django-registration-defaults"
    pip install avatar==1.0.5 # Set forum avatar images
    python manage.py syncdb   # Create admin user

    # Start Django dev server with Moot.it credentials given as OS environment variables
    MOOT_IT_FORUM_URL="https://moot.it/i/YOURFORUM" MOOT_IT_API_KEY="your-moot-it-api-key" MOOT_IT_API_SECRET="your-moot-it-api-secret" python manage.py runserver

Then visit `http://localhost:8000 <http://localhost:8000>`_ and you should see the forums anonymously.

Go to `http://localhost:8000/admin/ <http://localhost:8000/admin/>`_ to login as admin user.

Then visit `http://localhost:8000/ <http://localhost:8000/>`_ again to see the logged in version.

Various debug info is printed to *stdout* when you open the forum view.

Author
------

Mikko Ohtamaa (`blog <https://opensourcehacker.com>`_, `Facebook <https://www.facebook.com/?q=#/pages/Open-Source-Hacker/181710458567630>`_, `Twitter <https://twitter.com/moo9000>`_, `Google+ <https://plus.google.com/u/0/103323677227728078543/>`_)
