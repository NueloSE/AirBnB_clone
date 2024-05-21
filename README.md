# Airbnb Clone Project - Command Interpreter

![hbnb photo](./images/hbnb.png)
Welcome to the Airbnb clone project! This project is the first step toward building a full web application: the Airbnb clone. In this initial phase, you will create a command interpreter to manage your Airbnb objects.

## Background Context

Before starting, please familiarize yourself with the Airbnb concept. The command interpreter is an essential component of the project as it will facilitate various operations on Airbnb objects, such as creating new objects, retrieving existing objects, updating attributes, and more.

## What's a Command Interpreter?

A command interpreter, similar to the shell, allows users to interact with the application by executing commands. In the context of this project, the command interpreter will enable users to perform operations on Airbnb objects, such as creating, retrieving, updating, and deleting them.

## Learning Objectives

By working on this project, you will gain proficiency in the following areas:

- Creating a Python package
- Implementing a command interpreter in Python using the cmd module
- Writing and executing unit tests for a large project
- Serializing and deserializing a Class
- Handling datetime and UUID
- Using \*args and \*\*kwargs in functions
- Managing named arguments in functions

## Requirements

- Python scripts should be written using vi, vim, or emacs editors.
- All files should be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
- Each file should end with a new line.
- The first line of all files should be exactly #!/usr/bin/python3.
- A README.md file at the root of the project folder is mandatory.
- Code should adhere to the PEP 8 style guide.
- All modules, classes, and functions must have documentation strings.
- Unit tests should be written using the unittest module and executed using python3 -m unittest.
- All tests should pass both in interactive and non-interactive mode.

## Execution

The shell should work in both interactive and non-interactive modes. Interactive mode allows users to input commands directly, while non-interactive mode reads commands from a file.

### Interactive Mode:

```
$ ./console.py
(hbnb) help
```

### Non-Interactiv Mode:

```
$ echo "help" | ./console.py
(hbnb)
```
