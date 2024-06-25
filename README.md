<div align="center">
<h2>Project Management APIs</h2>

<img src="https://img.shields.io/badge/Python 3.12.0-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
<img src="https://img.shields.io/badge/Django 5.0.6-092E20?style=for-the-badge&logo=django&logoColor=green">
<img src="https://img.shields.io/badge/REST Framework 3.15.2-092E20?style=for-the-badge&logo=django&logoColor=red">

</div>

## Technologies

* Django for the backend application structure and ORM.
* Django Rest Framework for RESTful APIs.
* [djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) for JWT authentication.
* [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/) for API endpoints schema.

## REST API Endpoints

> have used `APPEND_SLASH=False`, so add `/` to end of the endpoint is prohibited.

* API Endpoints Schema `/api/docs`

### Users

- **GET /api/users:** Retrieve a list of authenticated users.
- **POST /api/users/register:** Create a new user.
- **POST /api/users/login:** Authenticate a user and return pair token.
- **GET /api/users/{user_uid}:** Retrieve details of a specific user.
- **PATCH /api/users/{user_uid}:** Allow users to update their own information.
- **DELETE /api/users/{user_uid}:** Allow users to delete their account.
- **POST /api/users/token/refresh:** Generate a new access token.

### Projects

- **GET /api/projects:** Retrieve a list of all projects.
- **POST /api/projects:** Create a new project.
- **GET /api/projects/{project_uid}:** Retrieve details of a specific project.
- **PATCH /api/projects/{project_uid}:** Update project details.
- **DELETE /api/projects/{project_uid}:** Delete a project.
- **GET /api/projects/{project_uid}/tasks:** Retrieve a list of all tasks in a particular project.
- **POST /api/projects/{project_uid}/tasks:** Create a new task in a project.

### Tasks

- **GET /api/tasks/{task_uid}/comments:** Retrieve a list of all comments on a task.
- **POST /api/tasks/{task_uid}/comments:** Create a new comment on a task.
- **GET /api/tasks/{task_uid}:** Retrieve details of a specific task.
- **PUT/PATCH /api/tasks/{task_uid}:** Update task details.
- **DELETE /api/tasks/{task_uid}:** Delete a task.

### Comments

- **GET /api/comments/{comment_uid}:** Retrieve details of a specific comment.
- **PUT/PATCH /api/comments/{comment_uid}:** Update comment details.
- **DELETE /api/comments/{comment_uid}:** Delete a comment.

## To run locally, follow these steps

### Clone the Repository

```shell
>> git clone https://github.com/imrand-dev/teamcollab-backend.git
>> cd teamcollab-backend
```

### Version Mismatch Resolution

If your version does not match mine (Python 3.12), follow these steps to update the project configuration.

* Update Pipfile:
    * Open `Pipfile` from your project directory.
    * Change the "python_version" to "3.10" in the "[requires]" section.
    ```py
    [requires]
    python_version = "3.10"
    ```
* Update Pipfile.lock:
    * Open `Pipfile.lock` from your project directory.
    * Change the "python_version" in the "requires" section to "3.10".
    ```py
    "requires": {
        "python_version": "3.10"
    },
    ```
* After making changes to the "Pipfile", regenerate the "Pipfile.lock" using `pipenv lock` command.

### Setup a Virtual Environment

Before creating a virtual environment, make sure you've already installed `pipenv` globally on your machine.

```shell
>> pipenv install (To create a new virtual env)
>> pipenv shell (To activate the virtual env)
```

### Install Dependencies

Although when you run `pipenv install` this command for the first time to create a virtual environment, all project dependencies are also installed inside the new environment.

So run this command kinda optional `pip install -r requirements/developemt.txt`.

### Setup Environment Variables

* Enter the main project directory `cd projectile`.
* There you'll see `.env.example` file, rename it to `.env` and fill out all the fields.

### Apply Migrations

I've used `SQLit3` as default database, so when you run `python manage.py migrate` this command, all tables will be stored in sqlite database.

```py
>> python manage.py makemigrations
>> python manage.py migrate
```

### Create a Superuser

I've already added a command that will generate a superuser with predefined fields.

```py
>> python manage.py superuser
```

- Then use this email and password
    - Email - johnsnow@gmail.com
    - Password - 123456

If you want to create a superuser on your own, run this command instead.

```py
python manage.py createsuperuser
```

### Run the Development Server

```py
>> python manage.py runserver
```

This command will start the development server, now open your browser and got to `http://127.0.0.1:8000/api/projects` to see all projects.

### Access Django Admin

Go to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials you created. This will allow you to manage users, tasks and other data using the Django admin interface.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests to contribute to the development of this project.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.