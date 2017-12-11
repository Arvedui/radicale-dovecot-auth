# Dovecot authentication plugin for Radicale.
# Copyright (C) 2017 Arvedui <arvedui@posteo.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__version__ = '0.2'


import socket

from radicale.auth import BaseAuth

from .dovecot_auth import DovecotAuth


SERVICE = "radicale"


class Auth(BaseAuth):
    """Authenticate user with dovecot auth service.

    Configuration:

    [auth]
    type = radicale_dovecot_auth

    auth_socket = path_to_socket
    """

    def get_connection(self):
        if not self.configuration.has_option('auth', 'auth_socket'):
            raise RuntimeError('auth_socket path must be set')

        return DovecotAuth(
                self.configuration.get('auth', 'auth_socket'), SERVICE)

    def is_authenticated(self, user, password):
        return self.is_authenticated2(None, user, password)

    def is_authenticated2(self, login, user, password):
        conn = self.get_connection()
        return conn.authenticate(user, password)
