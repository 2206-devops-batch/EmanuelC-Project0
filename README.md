# EmanuelC-Project0

# Requirements
Python and pip must be installed to proceed <br />
install Django by running command: <br />
```python -m pip install Django``` <br />
or ```python3 -m pip install Django```

# Django setup for blog app
run command to create database: ```python manage.py migrate``` <br /> 
to test if its working correctly run: <br />
```python manage.py runserver``` <br />
click on url, will display title and "No Items In List"
# Create user:
```python manage.py createsuperuser``` <br />
will ask to create account, use this to access backend to add items. but this isnt important for our assignment
# add tasks to app
in order to add tasks to the app run command in new terminal while runserver is on or turn it off and run command: <br />
``` python .\manage.py add_todo [username] [title] [description] 'True' ``` <br />
each argument wrapped under single qoutes to make it easier to create longer titles and descriptions. last argument will remain 'True' <br />
# create user
if you want to add more users run command: <br />
```python manage.py [username] ``` <br />
