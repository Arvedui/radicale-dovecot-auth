Radicale Dovecot Auth
#####################

Dovecot authentication plugin for Radicale.

Installation
============

.. code::

        python3 -m pip install --upgrade git+https://github.com/Arvedui/radicale-dovecot-auth


Configuration
=============

.. code::

        [auth]
        type = radicale_dovecot_auth

        auth_socket = path_to_socket
