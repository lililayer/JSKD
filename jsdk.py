import json
import os
import click

def DEBUG(log):
    print("\033[2m" + log + "\033[0m")
    
def Execute(program):
    path = program
    DEBUG("\nopening " + path)
    content = ""
    with open(path, 'r') as file:
        content = file.read()
    DEBUG("parsing content")
    data = json.loads(content)

    _content = ""
    for line in data["text"]:
        _content += line + '\n'

    path = data["name"]
    DEBUG("writing " + path)
    with open(path, 'w') as file:
        file.write(_content)

    DEBUG("runing : " + data["run_command"] + '\n')
    os.system(data["run_command"])

@click.command()
@click.option('--program', '-p', default="", help='JSON file name containing the program')
def main(program):
    if (program == ""):
        print("no such program to execute !")
        exit()
    
    Execute(program)
    
    DEBUG("\ndone, exiting")
    exit()

    
if __name__ == '__main__':
    main()
