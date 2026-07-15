# JSKD
run anything from a JSON file

## FUNCTIONALITY
Loads json then create a file named by `name`, then write the json's `text` section as its content and then run the command specified in `run_command`.

## USAGE

interpreted language example :
```json
{
    "name": "test.py",
    "run_command": "python3 test.py",
    "text": [
        "print(\"Hello, world !\")"
    ]
}
```

compiled language :
```json
{
    "name": "test.c",
    "run_command": "gcc test.c -o test && ./test",
    "text": [
        "#include <stdio.h>",
        "int main() {",
        "\tprintf(\"Hello, World!\");",
        "\treturn 0;",
        "}"
    ]
}
```

## EXECUTION
```bash
python3 jsdk.py -p path/to/program.json
```
