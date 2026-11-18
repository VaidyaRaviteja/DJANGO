# Employee directory with Django

The Employees project contains a Django employee app. Follow the detail route into the app to see how a request for an employee is handled.

- [Employee URL patterns](./Employees/app/urls.py)
- [Application code](./Employees/app)
- [Page templates](./Employees/templates)
- [Python dependencies](./Employees/requirements.txt)

## Local setup

Create and activate a Python virtual environment, then change into `Employees/` and install the dependencies with `python -m pip install -r requirements.txt`. Configure the project’s database settings before running `python manage.py migrate` and `python manage.py runserver`.
