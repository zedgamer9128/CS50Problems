import check50
import check50.rust
import os

@check50.check()
def exists():
    """main.rs exists"""
    check50.exists("src/main.rs")

@check50.check(exists)
def compiles():
    """main.rs compiles"""
    check50.rust.compile()

@check50.check(compiles)
def emma():
    """responds to name Emma"""
    check50.run("./hello").stdin("Emma").stdout("Emma").exit()

@check50.check(compiles)
def rodrigo():
    """responds to name Rodrigo"""
    check50.run("./hello").stdin("Rodrigo").stdout("Rodrigo").exit()
