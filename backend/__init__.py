from flask import Flask


def create_app():
    app = Flask(
        __name__,
        template_folder="../frontend/templates",
        static_folder="../frontend/static"
    )

    from backend.routes import main
    app.register_blueprint(main)

    return app