Radicale Dovecot Auth
#####################

Dovecot authentication plugin for Radicale.

Installation
============

From Source
-----------

.. code::

        pip3 install radicale-dovecot-auth

Debian
------

Packages are available here_

.. _here: https://debs.slavino.sk/pool/main/r/radicale-dovecot-auth/

Archlinux
---------

Packages are available in AUR for the `latest release`_ and current `master`_.

.. _latest release: https://aur.archlinux.org/packages/radicale-dovecot-auth/
.. _master: https://aur.archlinux.org/packages/radicale-dovecot-auth-git/



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

If you have a `/var/run/dovecot/auth-client` socket that is readable and writable by the radicale user/group, use that. Otherwise you may need to add a new auth_ socket to dovecot:

.. _auth: https://doc.dovecot.org/configuration_manual/service_configuration/

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

Only version 1.2 as described in the `Dovecot Wiki`_

.. _Dovecot Wiki: https://doc.dovecot.org/developer_manual/design/auth_protocol/
