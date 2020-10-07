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

When using socket authentication and systemd, check your radicale.service file. If it contains the following line (The default on Arch Linux contains this line):

.. code::

        RestrictAddressFamilies=~AF_PACKET AF_NETLINK AF_UNIX

Then the radicale service can't connect to a unix socket. Change the service file with:

.. code::

        # systemctl edit radicale
This opens the file /etc/systemd/system/radicale.service.d/override.conf in your text editor (creating it if necessary) and automatically reloads the unit when you are done editing. Add the following: 

.. code::

        [Service]
        RestrictAddressFamilies=
        RestrictAddressFamilies=~AF_PACKET AF_NETLINK

Authentication Backend
######################
DovecotAuth provides authentication against a Dovecot authentication
service using the PLAIN mechanism.

Only version 1.1 as described in the `Dovecot Wiki`_

.. _Dovecot Wiki: https://wiki2.dovecot.org/Design/AuthProtocol
