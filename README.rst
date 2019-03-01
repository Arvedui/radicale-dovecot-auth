Radicale Dovecot Auth
#####################

Dovecot authentication plugin for Radicale.

Installation
============

.. code::

        pip3 install radicale-dovecot-auth


Configuration
=============

Ensure that user running radicale has read and write permissions to the socket created by auth-userdb.

.. code::

        [auth]
        type = radicale_dovecot_auth

        auth_socket = path_to_socket

        # or tcp based
        auth_host = localhost
        auth_port = 10000

You may need to add a new auth_ socket to dovecot:

.. _auth: https://wiki.dovecot.org/Services#auth

.. code::

        unix_listener auth-client {
                path = path_to_socket
                mode = 0660
                user = radicale
                group = postfix
        }

Or tcp based:

.. code::

        inet_listener auth-client {
                address = localhost
                port = 10000
        }


Authentication Backend
######################
DovecotAuth provides authentication against a Dovecot authentication
service using the PLAIN mechanism.

Only version 1.1 as described in the `Dovecot Wiki`_

.. _Dovecot Wiki: https://wiki2.dovecot.org/Design/AuthProtocol
