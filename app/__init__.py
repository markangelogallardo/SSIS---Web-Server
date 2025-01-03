from flask import Flask
from flask_mysqldb import MySQL
from flask_bootstrap import Bootstrap
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, BOOTSTRAP_SERVE_LOCAL, CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET 
from flask_wtf.csrf import CSRFProtect
import cloudinary

# Configuration       

mysql = MySQL()
bootstrap = Bootstrap()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        MYSQL_USER=DB_USERNAME,
        MYSQL_PASSWORD=DB_PASSWORD,
        MYSQL_DB=DB_NAME,
        MYSQL_HOST=DB_HOST,
        BOOTSTRAP_SERVE_LOCAL=BOOTSTRAP_SERVE_LOCAL
    )

    cloudinary.config( 
        cloud_name = CLOUD_NAME, 
        api_key = CLOUDINARY_API_KEY, 
        api_secret = CLOUDINARY_API_SECRET , 
        secure=True
    )
    bootstrap.init_app(app)
    mysql.init_app(app)
    CSRFProtect(app)

    from .student import student_bp as student_blueprint
    app.register_blueprint(student_blueprint)
    from .program import program_bp as program_blueprint
    app.register_blueprint(program_blueprint)
    from .college import college_bp as college_blueprint
    app.register_blueprint(college_blueprint)


    return app