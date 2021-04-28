#!/usr/bin/python3

# source code : http://urlregex.com/
# test file: https://mathiasbynens.be/demo/url-regex

from sys import argv
import re

def url_validator(line):
    url_patt='http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    return re.search(url_patt,line)


if __name__=='__main__':

    #filepath='./SHOULD_MATCH'
    filepath='./SHOULD_NOT_MATCH'

    if len(argv) > 1:
        filepath=argv[1]

    print(filepath)

    #url_patt='http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    matches=0
    with open(filepath) as fp:
        lines = fp.readlines()
        for line in lines:
            found = url_validator(line)
            if found:
                matches+=1
                print(found.group())
        print('N of lines:',len(lines),'N of matches:',matches)
