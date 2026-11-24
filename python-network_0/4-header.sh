#!/bin/bash
# Send a custom header and display the response body
curl -s -H 'X-HolbertonSchool-User-Id: 98' "$1"
