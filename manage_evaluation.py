# encoding: utf-8
"""
@author: chenxiyue
@contact: chenxiyue@126.com
@software: PyCharm
@file: manage_evaluation.py
@time: 2024/7/2 15:26
"""

from flask_script import Manager, Server as _Server

from evaluation.app import app
from evaluation.config import DevConfig, ProdConfig


class Server(_Server):
    def __call__(self, app, host, port, use_debugger, use_reloader,
                 threaded, processes=None, passthrough_errors=None, ssl_crt=None, ssl_key=None):
        # we don't need to run the server in request context
        # so just run it directly

        if use_debugger:
            app.config.from_object(DevConfig)
        else:
            app.config.from_object(ProdConfig)

        app.run(host=host,
                port=port,
                debug=use_debugger,
                use_debugger=use_debugger,
                use_reloader=use_reloader,
                threaded=threaded,
                processes=processes,
                passthrough_errors=passthrough_errors,
                **self.server_options)

manager = Manager(app)

manager.add_command('debug', Server(host='0.0.0.0', port=6666, use_debugger=True, threaded=True, use_reloader=False))
manager.add_command('product', Server(host='0.0.0.0', port=6666, use_debugger=False, threaded=True, use_reloader=False))

if __name__ == '__main__':
    manager.run()