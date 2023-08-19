import config as c

from app import app


if __name__ == "__main__":
    app.run(debug=c.DEBUG_MODE, port=c.PORT, host=c.HOST)
