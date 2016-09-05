# flask-todolist
It's a tiny flask todolist website, and used to new, edit, delete and to remark whether it's done.

# deploy
## requirements
### Python
  It's ran in Python3.5, but It's not relied on specific Python version.
  However, if you wanna ran it into 2.x, please remember to change basic.py of  a dependency 3rd package-ForgeryPy's:range->xrange(Python3.x doesn't support xrange) after installing it
  Then you can install 3rd packages by pip -r requirements.txt
### Databse
  It uses mysql, but you don't  necessarily use the only one. Change SQLALCHEMY_DATABASE_URI in config.py to cater your envirment.
  
### deployment
  * todolist.py
  It helps to develop, test, you can use: python todolist.py command(commands:dev-debug, forged-product test data, test-run test cases)
  * wsgi.py
  for deployment using unicorn
  * Due to my own environment, I don't completely test the environment by using unicorn + niginx *

### development
  * auth
  auth includes:register, login and loginout modules, and it's simple and not use email to validate, and passowrd is plaintext stored.
  * main
  main includes:show all list of current user, add, edit and delete a todo. What's more, users can mark whether one event is done.
  * What's more
  If you wantna add more apps such as reminding and email support , you can do by Blueprint as following:
    1. add a python package in app directory, for example newapp, and edit __init__.py in the new app:  
    
    ``
      from flask import Blueprint
      newapp = Blueprint('newapp', __name__)
   ``             

    2. in views.py of new app, add import: 
    
    ``
      from . import newapp
    ``   
      
    3. in app directory, edit create_app in __init__.py to register new app:  
    
    ``
      from .newapp import newapp as newapp_blueprint
      app.register_blueprint(newapp_blueprint, url_prefix='/xxx')
    ``      
