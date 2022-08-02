HOW TO RUN:

1. Clone the remote repository to your local system

2. Install the dependencies using the requirements.txt file

3. Run this command:
pip install -r /path/to/requirements.txt

4. Inside the folder: api_rest/clients

    Run the following commands:

    python3 manage.py makemigrations

    python3 manage.py migrate

5. Run python3 manage.py runserver

6. Visit localhost or http://127.0.0.1/

7: Start making API requests


API ENDPOINTS:
1. Get all registered clients and add a new client: http://127.0.0.1/api/clients/

2. Obtains the detail and can update a single client through its Primary Key:
http://127.0.0.1/api/clients/{pk}


BODY EXAMPLES FOR A API REQUEST:

Create a new client:

{
    "name": "Daniel", "lastname": "Ortiz",
    "email": "my_mail@example.com",
    "password": "12345",
    "username": "myusername"
}

Update an entire client:

{
    "name": "New Name", "lastname": "New lastname",
    "email": "change@example.com",
    "password": "123456",
    "username": "myusername_new",
    "height": 185,
    "weight": 70.5,
    bmi: 20.1,
    "geb": 1,
    "eta": 2,
}
