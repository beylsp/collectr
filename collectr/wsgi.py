from collectr import factory

app = factory.create_app()


def app():
    app.run()


if __name__ == '__main__':
    app.run()
