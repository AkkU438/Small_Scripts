import os
import pickle
from datetime import datetime

todo = []
todo_file = "todo.pkl"


# I don't really feel like coding right now, so I'm just gonig to just do some simple stuff that I don't know if I'm going to use.

def display_todo(): 
    if len(todo) == 0:
        print("no tasks todo please enter a task")
    else: 
        for i, task in enumerate(todo):
            print(f"{i + 1}, {task}")
    return

def functionaltiy():

    return 

def main(): 
    display_todo()
    return 