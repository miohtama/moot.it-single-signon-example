Moot.it forum integration example with Django
-----------------------------------------------

Single-sign-on JavaScript embeddable forms for Django from `moot.it <http://moot.it>`_.

Running
---------

First get `virtualenv <https://pypi.python.org/pypi/virtualenv/>`_ to your OS.

Example (Python 2.7)::

    git clone git@github.com:miohtama/moot.it-single-signon-example.git
    cd moot.it-single-signon-example
    virtualenv venv  # Use virtualenv command for your Python
    source venv/bin/activate
    pip install Django  # Install django
    python manage.py syncdb   # Create admin user

    # Start Django dev server with Moot.it credentials given as OS environment variables
    MOOT_IT_FORUM_URL="https://moot.it/i/YOURFORUM" API_KEY="your-moot-it-api-key" API_SECRET="your-moot-it-api-secret" manage.py runserver

Then visit `http://localhost:8000 <http://localhost:8000>`_ and you should see the forums anonymously.

Go to `http://localhost:8000/admin/ <http://localhost:8000/admin/>`_ to login as admin user.

Then visit `http://localhost:8000/ <http://localhost:8000/>`_ again to see the logged in version.

Various debug info is printed to *stdout* when you open the forum view.

Author
------

Mikko Ohtamaa (`blog <https://opensourcehacker.com>`_, `Facebook <https://www.facebook.com/?q=#/pages/Open-Source-Hacker/181710458567630>`_, `Twitter <https://twitter.com/moo9000>`_, `Google+ <https://plus.google.com/u/0/103323677227728078543/>`_)
