from flask.views import MethodView
import os

def register(app):
    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>", methods=["GET", "HEAD", "OPTIONS"])
    def try_files_static_index(path):
        static_path = os.path.join(app.static_folder, path)
        if os.path.exists(static_path) and not os.path.isdir(static_path):
            return app.send_static_file(path)
        else:
            return app.send_static_file("index.html")