import re

def welcome_msg():
    print("Welcome to mdalib game!, In this game you are required to enter (adjectives and nouns) in your terminal and you will get a random sentence")


########## Test Functions #########   
def read_template(text):
    try:
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

########## input Functions #########  
def new_user_input(lst):
    input_lst = []
    for i in lst:
        user_input = input(f"Enter a/an {i} \n")
        input_lst.append(user_input)
    return input_lst


def user_input_file(merged_inputs):
    with open("./assets/new_file.txt", "w") as file:
        file.write(merged_inputs)

########## Display Function #########
if __name__ == "__main__":
    welcome_msg()
    file_text = read_template("./assets/liar_in_the_game.txt")
    # file_text = read_template("./assets/steal.txt")
    # file_text = read_template("./assets/dark_and_stormy_night_template.txt")
    input_stripped, input_parts = parse_template(file_text)
    user_input = new_user_input(input_parts)
    result = merge(input_stripped, user_input)
    print(result)
    user_input_file(result)