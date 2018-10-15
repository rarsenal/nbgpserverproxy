# vim: set et sw=4 ts=4:
import os
import getpass
import pwd
import tempfile

from urllib.parse import urlunparse, urlparse

from tornado import web

from notebook.utils import url_path_join as ujoin
from notebook.base.handlers import IPythonHandler

from nbserverproxy.handlers import SuperviseAndProxyHandler


class AddSlashHandler(IPythonHandler):
    """Handler for adding trailing slash to URLs that need them"""
    @web.authenticated
    def get(self, *args):
        src = urlparse(self.request.uri)
        dest = src._replace(path=src.path + '/')
        self.redirect(urlunparse(dest))


class GPServerProxyHandler(SuperviseAndProxyHandler):
    '''Manage an Genepattern Server instance.'''

    name = 'genepattern'

    def get_env(self):
        env = {}

        if not os.environ.get('USER', ''):
            env['USER'] = getpass.getuser()

        return env

    def get_cmd(self):
        return [
            'genepattern',
            '-p ' + str(self.port)
        ]

def setup_handlers(web_app):
    web_app.add_handlers('.*', [
        (ujoin(web_app.settings['base_url'], 'gp/(.*)'), GPServerProxyHandler, dict(state={})),
        (ujoin(web_app.settings['base_url'], 'gp'), AddSlashHandler)
    ])
