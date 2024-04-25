#!/bin/bash
# Script that takes in a URL, sends a POST request to the passed URL, and shows the body of the response, A var email must be sent with the value hr@holbertonschool.com, A var subject must be sent with the value I will always be here for PLD
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
