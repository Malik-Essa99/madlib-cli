import re

def read_template(text):
    try:
        print("Welcome to mdalib game!, In this game you are required to enter adjectives and nouns in your terminal and you will get a random sentence")
        with open(text, "r") as template:
            file = template.read()
            return (file)
    except FileNotFoundError:
        raise 

def parse_template(text):
    file = text
    stripped = re.sub("{[^{}]+}","{}", file)
    parts = re.findall(r'{([^}]+)}',file)
    return (stripped,tuple(parts))

def merge(stripped,parts):
    result = stripped
    for i in parts:
        result = result.replace("{}",i,1)
    return (result)