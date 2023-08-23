import config as c

from app import app


if __name__ == "__main__":
    app.run(debug=c.debug_mode, port=c.port, host=c.host)
