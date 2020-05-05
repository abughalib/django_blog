# Django Blog application

For preview -> [goto preview folder](preview/)

**Requirement**<br><hr>
python 3.6 or higher<br>
`pip install django`<br>
`pip install pillow`
<hr>

<h2>Run Application<h2>
  
  `python manage.py runserver`

<h2>Change the following<h2>

1. SECRET KEY in settings.py

**To use password reset using email**

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'email'
EMAIL_HOST_PASSWORD = os.environ.get('email_pass')

**Alternately you can use WebApi**
