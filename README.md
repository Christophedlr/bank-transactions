# bank-transactions
Bank Transactions is an Django CMS for write the transactions of bank accounts

## Installation
* Download the website
* Unzip files in choose server directory
* Create the venv directory : 
`python -m venv venv`
* Install dependencies in venv (venv activated) :
`python -m pip -r requirements.txt`
* Configure Apache/Nginx to used WSGI
* Fill settings.ini (Secret key is an random characters used by generate password and other security elements)
* Start web server

## Usage
## Create admin user
In venv activated and in a _bank_ directory, type :
`python manage.py createsuperuser` for create a superuser

### Accounts
User accounts required an admin validation.
WARNING ! RGPD respect is required in Europe.

### Administration
For manage users and other elements, used the Django administration :
`/admin` URL route. Superuser is required for access.

### Bank account
In list of bank accounts, click in account name for list all transactions.
