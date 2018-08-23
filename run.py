from my_api.instance import config
from my_api.instance import config

app = create_app(config.DevelopmentConfig)

if __name__ == '__main__':
    app.run()