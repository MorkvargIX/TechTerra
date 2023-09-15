from app import app, config


if __name__ == "__main__":
    app.run(debug=config.debug_mode, port=config.port, host=config.host)
