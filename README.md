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
  
