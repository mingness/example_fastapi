# Example FastAPI Application

This WIP repository is an example application that uses what I consider good
practices for developer experience, testing, and deployment. Best practices
is to automate as much as possible, from pre-commit hooks, to automatic
running of tests on every commit. Other good practices that cannot be shown
in this repository easily is the presence of at least a production and
staging environment, so there is a place to test and check changes before
they go live.

FastAPI is a great way to build apis that keeps code efficient. It
integrates use of pydantic for object models, makes definition of routes
intuitive, and creates documentation out of the box.

This application includes endpoints for sensor
registration and retrieval, which will save data to a postgres database.

The repository uses alembic to track changes in the database, and easily
switch between versions.

TODO:
1. Tests could be configured to run on Github Actions with every commit.
2. Use certs and https in nginx. Ideally urls publicly available should use
   https.
3. Add user authentication. Ideally user authentication would be integrated
   into the middleware, so that it runs on every call. There would be a
   login endpoint, and an endpoint that provides a temporary token that
   would be stored in the `Authorization` header.

## How to use locally

This application uses docker to deploy the application, and you will need a
Docker account. Please ensure the prerequisites below are implemented before
running the program.

To run the program, please run at command line,
```commandline
docker-compose up -d --build
```

To shut down the application, run
```commandline
docker-compose down
```

To interact with the application, you can use Postman to construct calls to
the API with a GUI. The host is http://locahost, and the route is `/sensors`.
For example, a call for all sensors would be GET http://localhost/sensors

This can also be done via command line with curl.

To add a sensor,
```commandline
curl -X POST http://localhost/sensors -H 'Content-Type: application/json' -d '{"device_id":"device_id1"}'
```

To get one sensor with id 1,
```commandline
curl http://localhost/sensors/1
```

To get all sensors,
```commandline
curl http://localhost/sensors
```

### Prerequisites

1. Install Docker and Docker Compose
2. Log into your docker account
3. copy `.env-sample` to `.env`, and feel free to change the password - this
   sets environment variables for the database

## Development

### Prerequisites
if you will develop the repo, a prerequisite is running `pre-commit`.
`pre-commit` is already included as a dependency, so if all packages are
installed, you just need to run at the command line

```commandline
pre-commit install
```

to run the configured pre-commit hooks before a committing.

The hooks that are run are
- built in hooks to remove extra trailing white space, and an extra line
  return as needed at the end of a file
- `isort` sorts the imports
- `black` is an opinionated code formatter that will automatically edit your
  files. includes a default width of 88 characters
- `flake8` is also a code formatter, that checks for errors, and complexity,
  asking you to fix the errors.

You'll need to have all hooks pass before the commit can happen. Pre-commit
usually runs only on files added in the commit.


### Configuring Pycharm

This project uses poetry for package management. You can select the Python
interpreter to be a poetry interpreter.

To ensure the tests run correctly and are visible to Pycharm, you may need
to add the application folder and test folders to PYTHONPATH. You can do
this project-wide by going into the Settings, navigating to the Python
interpreter. You'll select from a menu or drop down "Show all." Then click
on the directory icon to see the paths the interpreter will search through.
Manually add your application and test folders.
