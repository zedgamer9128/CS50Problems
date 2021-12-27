import check50
import check50.rust
import re
import os

@check50.check()
def exists():
    """main.rs exists"""
    check50.exists("src/main.rs")
    check50.include("test.rs")


@check50.check(exists)
def compiles():
    """plurality compiles"""
    # rename main.rs
    os.rename("src/main.rs", "src/main_bak.rs")
    plurality = open("src/main_bak.rs").read()
    testing = open("test.rs").read()
    with open("src/main.rs", "w") as f:
        f.write(plurality)
        f.write("\n")
        f.write(testing)
    print(check50.run("ls").stdout())
    check50.rust.compile()

@check50.check(compiles)
@check50.hidden("vote function did not return true")
def vote_finds_name_first():
    """vote returns true when given name of first candidate"""
    check50.run("cargo test test_vote -- 0 0").exit(0)

@check50.check(compiles)
@check50.hidden("vote function did not return true")
def vote_finds_name_middle():
    """vote returns true when given name of middle candidate"""
    check50.run("cargo test test_vote -- 0 1").exit(0)

@check50.check(compiles)
@check50.hidden("vote function did not return true")
def vote_finds_name_last():
    """vote returns true when given name of last candidate"""
    check50.run("cargo test test_vote -- 0 2").stdout("true").exit(0)

@check50.check(compiles)
@check50.hidden("vote function did not return false")
def vote_returns_false():
    """vote returns false when given name of invalid candidate"""
    check50.run("cargo test test_vote -- 0 3").stdout("false").exit(0)

@check50.check(compiles)
@check50.hidden("vote function did not correctly update vote totals")
def first_vote_totals_correct():
    """vote produces correct counts when all votes are zero"""
    check50.run("cargo test test_vote -- 0 4").stdout("1 0 0").exit(0)

@check50.check(compiles)
@check50.hidden("vote function did not correctly update vote totals")
def subsequent_vote_totals_correct():
    """vote produces correct counts after some have already voted"""
    check50.run("cargo test test_vote -- 0 5").stdout("2 8 0").exit(0)

@check50.check(compiles)
@check50.hidden("vote function modified vote totals incorrectly")
def invalid_vote_votes_unchanged():
    """vote leaves vote counts unchanged when voting for invalid candidate"""
    check50.run("cargo test test_vote -- 0 6").stdout("2 8 0").exit(0)

@check50.check(compiles)
@check50.hidden("print_winner function did not print winner of election")
def print_winner0():
    """print_winner identifies Alice as winner of election"""
    check50.run("cargo test test_vote -- 0 7").stdout("^Alice\n?$").exit(0)

@check50.check(compiles)
@check50.hidden("print_winner function did not print winner of election")
def print_winner1():
    """print_winner identifies Bob as winner of election"""
    check50.run("cargo test test_vote -- 0 8").stdout("^Bob\n?$").exit(0)

@check50.check(compiles)
@check50.hidden("print_winner function did not print winner of election")
def print_winner2():
    """print_winner identifies Charlie as winner of election"""
    check50.run("cargo test test_vote -- 0 9").stdout("^Charlie\n?$").exit(0)

@check50.check(compiles)
@check50.hidden("print_winner function did not print both winners of election")
def print_winner3():
    """print_winner prints multiple winners in case of tie"""
    result = check50.run("cargo test test_vote -- 0 10").stdout()
    if set(result.split("\n")) - {""} != {"Alice", "Bob"}:
        raise check50.Mismatch("Alice\nBob\nCharlie\n", result)

@check50.check(compiles)
@check50.hidden("print_winner function did not print all three winners of election")
def print_winner4():
    """print_winner prints all names when all candidates are tied"""
    result = check50.run("cargo test test_vote -- 0 11").stdout()
    if set(result.split("\n")) - {""} != {"Alice", "Bob", "Charlie"}:
        raise check50.Mismatch("Alice\nBob\nCharlie\n", result)
