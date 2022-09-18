# proxy-demo

Demo project of HTTP proxy server with JWT encoded header injection support.

Requirement: Python 3.10, SQLAlchemy, Flask, uWSGI

&nbsp;  

## Local server setup

Note that local server usage is for testing only!

Install the requirements:

    $ pip3 install -r requirements.txt

Run server:

    $ python3 -m proxy.uwsgi

For older Flask versions, you can use FLASK_ENV to enable development config:

    $ FLASK_ENV=Development python3 -m proxy.uwsgi

Status page should be available now: http://localhost:8077/api/v1/status

Default server public port is 8077.

You can change it by setting environment variable HTTP_PORT via CLI:

    $ HTTP_PORT=7171 python3 -m proxy.uwsgi

or via [.env](.env) file.


## Docker compose management

Build docker image:

    $ make build

Start proxy:

    $ make

    or

    $ make start

Status page should be available now: http://localhost:8077/api/v1/status

Stop proxy:

    $ make stop

Restart proxy:

    $ make restart

Display docker logs:

    $ make logs


Default server public port is 8077.

You can change it by setting environment variable HTTP_PORT via CLI:

    $ HTTP_PORT=7171 make build
    $ HTTP_PORT=7171 make start
    $ HTTP_PORT=7171 make test

or via [.env](.env) file.


## Automatic tests

Python unittest is using to cover test cases.
Below installs test env requirements and run the tests.

    $ make test


## Logs

Logs are stored to the 'logs' dir inside container.

Logs dir is also exposed via docker-compose "volumes", so you can check log files directly at 'logs' dir where docker-compose is called from.

system.log - Contains system events and requests data

db.log - Contains database related events

uwsgi.log - Contains uWSGI HTTP server events

## Documentation

Python documentation is avaiable:

    $ python3 -c "import proxy; help(proxy)"
