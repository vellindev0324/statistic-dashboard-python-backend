from app import create_app
import os, certifi

os.environ["SSL_CERT_FILE"] = certifi.where()

app = create_app()


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=10000)
