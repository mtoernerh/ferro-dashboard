from app.app import create_app
from waitress import serve

app = create_app()

if __name__ == "__main__":
    #serve(app.server, host="0.0.0.0", port=8282)
    app.run(host="0.0.0.0", port=8282, debug=True)