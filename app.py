import factory

app = factory.create_app(config_name='DEVELOPMENT')
app.app_context().push()

if __name__ == "__main__":
    app.run()
