#!/bin/bash

if [ ! -d "./.venv/lib/python3.5/" ]; then
  echo "./.venv/lib/python3.5/ does not exist. Will initiate virtual environment"
  virtualenv -p python3 .venv
else
  echo "./.venv/lib/python3.5/ already exist. Will not initiate virtual environment again."
fi