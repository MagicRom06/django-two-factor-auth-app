# django-two-factor-auth-app
A simple django app using allauth_2fa package

# Requirements
The app require python 3.8, django 3.2 with django-allauth-2fa module.<br>
The goal is to simply test 2fa authentification<br>
The database is PostgreSQL

# How to test
Go to http://two-factorauth-app.herokuapp.com/<br>
Create a new account<br>
Go to "Activate 2fa"<br>
Scan the QR code with QRcode generator like Google Authenticator and generate tokens<br>
Logout and log again <br>
The app will ask you the token once logged.
