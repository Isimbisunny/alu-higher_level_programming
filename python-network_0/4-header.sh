#!/bin/bash
# Send a custom header and display the response body
curl -s -X GET -H 'X-HolbertonSchool-User-Id: 98' "http://$1"
