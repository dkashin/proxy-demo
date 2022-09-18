#!/bin/bash

curl \
http://localhost:8080/api/v1/echo \
-H "Content-Type: application/json" \
-d '{ "payload": "my_payload" }' \
-v | jq .
