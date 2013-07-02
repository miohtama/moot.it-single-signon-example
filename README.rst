Moot.it forum integration example with Django
-----------------------------------------------

Single-sign-on JavaScript embeddable forms for Django from `moot.it <http://moot.it>`_.

Running
---------

Example::

    git clone ... mootexample
    cd mootexample
    virtualenv venv
    source venv/bin/activate
    pip install Django
    python manage.py syncdb   # Create admin user

    # Start Django dev server with Moot.it credentials given as OS environment variables
    API_KEY="your-moot-it-api-key" API_SECRET="your-moot-it-api-secret" manage.py runserver

Then visit `http://localhost:8000 <http://localhost:8000>`_ and you should see the forums anonymously.

Go to `http://localhost:8000/admin/ <http://localhost:8000/admin/>` to login as admin user.

Then visit `http://localhost:8000/ <http://localhost:8000/> again to see the logged in version.

Various debug info is printed to *stdout* when you open the forum view.

Author
------

Mikko Ohtamaa (`blog <https://opensourcehacker.com>`_, `Facebook <https://www.facebook.com/?q=#/pages/Open-Source-Hacker/181710458567630>`_, `Twitter <https://twitter.com/moo9000>`_, `Google+ <https://plus.google.com/u/0/103323677227728078543/>`_)
