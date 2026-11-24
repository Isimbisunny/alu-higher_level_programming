#!/bin/bash
# Display the HTTP methods accepted by a URL
curl -s -I "$1" | grep -i '^Allow:' | cut -d' ' -f2-
