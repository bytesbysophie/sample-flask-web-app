from datetime import datetime
from flask import Flask, render_template

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'sample-flask-web-app.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple landing page
    @app.route('/')
    def hello():
        return 'Hello, You!'

    # landing page build with a html template
    @app.route('/template')
    def template():
        return render_template('template-test.html')

    # landing page build with a html template using a parameter
    @app.route('/template-param')
    def template_param():
        return render_template('template-param-test.html', current_timestamp=datetime.now())

    return app
