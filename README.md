# Django Blog application

For preview -> [goto preview folder](preview/)

### Requirement<br><hr>
**python 3.6 or higher <br>
`pip install django`<br>
`pip install pillow`<br>
<hr>

#### Run Application <br>
  
  `python manage.py runserver`

**Change the following <br>

SECRET KEY in settings.py

**To use password reset using email**

`EMAIL_HOST = 'smtp.gmail.com'`<br>
`EMAIL_PORT = '587'`<br>
`EMAIL_USE_TLS = True`<br>
`EMAIL_HOST_USER = 'email'`<br>
`EMAIL_HOST_PASSWORD = os.environ.get('email_pass')`

**Alternately you can use WebApi for this purpose.**
