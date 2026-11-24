#!/bin/bash
# Display the size in bytes of a URL response body
curl -s "$1" | wc -c
