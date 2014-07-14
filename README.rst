bananas
=======


Local database setup
--------------------

 #. Create PostgreSQL user with id matching your UNIX username::

    $ sudo -u postgres createuser $(whoami) -SDR

 #. Create a database owned by this user::

    $ sudo -u postgres createdb -E UTF-8 -O $(whoami) bananas

 #. Check we can connect to this database::

    $ /usr/bin/psql bananas
    psql (9.1.2)
    Type "help" for help.
    
    bananas=> \q

Syncing with the live site
--------------------------

Sync database::

    $ ./manage.py sync_database
