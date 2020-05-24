# Dovecot authentication plugin for Radicale.
# Copyright (C) 2017-2019 Arvedui <arvedui@posteo.de>
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

from radicale.auth import BaseAuth

from radicale_dovecot_auth.dovecot_auth import DovecotAuth
from radicale_dovecot_auth.__about__ import *

from contextlib import suppress


SERVICE = "radicale"


class Auth(BaseAuth):
    """Authenticate user with dovecot auth service.

    Configuration:

    [auth]
    type = radicale_dovecot_auth

    auth_socket = path_to_socket

    # or tcp based
    host = example.com
    port = 10000
    """

    def get_connection(self):
        kwargs = {}

        with suppress(KeyError):
            kwargs['socket_path'] = self.configuration.get('auth', 'auth_socket')
            kwargs['host'] = self.configuration.get('auth', 'auth_host')
            kwargs['port'] = self.configuration.get('auth', 'auth_port')

        if not ('socket_path' in kwargs or {'host', 'port'} <= set(kwargs)):
            raise RuntimeError('auth_socket path or auth_host and auth_port must be set')

        return DovecotAuth(SERVICE, **kwargs)

    def is_authenticated(self, user, password):
        return self.is_authenticated2(None, user, password)

    def is_authenticated2(self, login, user, password):
        conn = self.get_connection()
        return conn.authenticate(user, password)

    def login(self, login, password):
        return login if self.is_authenticated(login, password) else ""
