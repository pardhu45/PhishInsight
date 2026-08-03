from backend import create_app

app = create_app()
app.secret_key = "phishinsight-secret-key"


if __name__ == "__main__":
    app.run(debug=True)