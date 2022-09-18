# proxy-demo

Demo project of HTTP proxy server with JWT encoded header injection support.

&nbsp;  
&nbsp;  

## Local server setup

Note that local server usage is for testing only!

Install the requirements:

    $ pip install -r requirements.txt

Run server:

By default, the proxy runs on port 5000. This can be changed in the [config file](proxy/config.py).

    $ python3 -m proxy

At this point, we should be able to browse: http://localhost:5000/  
Please remember to hit Ctrl+c to stop the web server when done.


## Automatic tests
Python tests are available using unittest/PyUnit via Makefile or manually.  
_Note: depending on how the proxy was started, may require ` sudo chmod o+w logs/* ` (not if in production)._

- Run ` make test ` to install requirements and run the tests.
- Or [install requirements](#set-up-and-install) and manually run ` python3 -m unittest tests/test_* `.

An extra basic test is available in Bash script using curl and it tests proxy [running manually](#running-the-proxy-server), [containerised](#containerise-with-the-dockerfile) or [composed](#run-the-docker-compose):

    $ bash tests/curl-post.bash


## The class to generate JWT
With the python console and the [class that generates JWT](proxy/Token.py), we can get a Token:

    $ python3
    >>> from proxy.Token import Token
    >>> user = 'fernando@github.com'
    >>> t = Token(user)
    >>> t.jwt


## Containerise with the Dockerfile
_I assume that you have docker engine running. If not, please see [Get Docker](https://docs.docker.com/get-docker/)._

If you rather run the proxy in a single container, run:

    $ docker run --rm -d -p 5000:5000 --name proxy $(docker build -f Dockerfile -t proxy . -q)

To know IP and Port to the containerised app:

    $ docker inspect proxy | grep -e IPAddr.*[0-9] -e HostPort | sed 's/[^0-9\.]//g' | sort -u

After this, we should be able to browse: http://\<container IP\>:5000/  

To stop container and clean image, use:

    $ docker stop proxy && docker image rm proxy


## Run the Docker compose
_I assume that you have docker compose installed. If not, please see [Install Docker Compose](https://docs.docker.com/compose/install/)._

There are Makefile rules to simplify this option. See the list of commands:

- ` $ make ` to build and run (up) the application.
    - or run `$ make build; make run ` _(note: run already calls build)_.
- ` $ make stop ` and ` make start ` to start the container.
- ` $ make rm ` to remove compose service, container, image.

The default HTTP proxy PORT is 5000 and set in [.env](.env). The port can be changed:

    $ HTTP_PORT=8080 make up


## Logs
By default, logs are recorded in the 'logs' directory in the project's root. However,
if you [containerise](#containerise-with-the-dockerfile) the proxy, 
logs will be inside the container. And if you [docker compose](#run-the-docker-compose), 
the container will use the hosts' dirs as in [Running the proxy](#running-the-proxy-server).

Please see [docs/logs](docs/logs) if you wish to access samples of the generated logs.


## Documentation
Please try from python console:

    $ python3
    >>> import proxy
    >>> help(proxy)

Or try from command line:

    $ python3 -c "import proxy; help(proxy.config)"

All documentation can be found in [docs](docs).


## To do

* Document separation of server from proxy.\__main__
* Configure rotation of log files.
* Review docstring in db.py.

