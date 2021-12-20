#!/bin/bash
#bash file to run the autolog script and flask server simultaneously

# launch the flask server and put it in the background
export FLASK_APP=flask_app

flask run -h 0.0.0.0 -p 80

wait -n

exit $?