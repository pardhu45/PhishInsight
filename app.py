from backend import create_app
from backend.extensions import init_db

app = create_app()
app.secret_key = "phishinsight-secret-key"

init_db()


if __name__ == "__main__":
    app.run(debug=True)