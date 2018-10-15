from nbgpserverproxy.handlers import setup_handlers

# Jupyter Extension points
def _jupyter_server_extension_paths():
    return [{
        'module': 'nbgpserverproxy',
    }]

def _jupyter_nbextension_paths():
    return [{
        "section": "tree",
        "dest": "nbgpserverproxy",
        "src": "static",
        "require": "nbgpserverproxy/tree"
    }]

def load_jupyter_server_extension(nbapp):
    setup_handlers(nbapp.web_app)
