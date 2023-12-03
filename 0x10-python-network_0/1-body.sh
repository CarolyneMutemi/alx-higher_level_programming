#!/bin/bash
# Sends a GET request to the URL, and displays the body of the response.
if [ "$(curl -sI "$1" | grep HTTP | cut -d " " -f 2)" = '200' ];then curl -s "$1";fi
