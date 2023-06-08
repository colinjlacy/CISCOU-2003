# JSON: Everything You Need to Know in 30 Minutes

This repo contains all of the demo code used in the Cisco U. Theater session CISCOU-2003, presented at Cisco Live in 2023.

## To start

Once you've cloned the repo, run the following to install dependencies:
```
$ pip install -r requirements.txt
```

From there, you can start up the demo API server by running the `00-server.py` file in the background.

## MongoDB

Follow the instructions [here](https://www.mongodb.com/docs/manual/installation/) to install and run MongoDB locally.  Once it's running, make sure that you have a database called `local`.  The code in the `08` and `09` Python files expects that database to exist.