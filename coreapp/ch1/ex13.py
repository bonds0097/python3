#!/usr/bin/env python3

import re

def typename(object):
    # Get the type as a string.
    type_string = str(type(object))
    # Parse the string for the relevant data.
    pattern = re.compile('<class \'(.*)\'>')
    match = pattern.match(type_string)

    return match.group(1)
