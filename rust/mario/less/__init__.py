import check50
import check50.rust

@check50.check()
def exists():
    """main.rs exists"""
    check50.exists("src/main.rs")
    check50.include("1.txt", "2.txt", "8.txt")

@check50.check(exists)
def compiles():
    """main.rs compiles"""
    check50.rust.compile()

@check50.check(compiles)
def test_reject_negative():
    """rejects a height of -1"""
    check50.run("cargo run").stdin("-1").reject()

@check50.check(compiles)
def test0():
    """rejects a height of 0"""
    check50.run("cargo run").stdin("0").reject()

@check50.check(compiles)
def test1():
    """handles a height of 1 correctly"""
    out = check50.run("cargo run").stdin("1").stdout()
    check_pyramid(out, open("1.txt").read())

@check50.check(compiles)
def test2():
    """handles a height of 2 correctly"""
    out = check50.run("cargo run").stdin("2").stdout()
    check_pyramid(out, open("2.txt").read())

@check50.check(compiles)
def test8():
    """handles a height of 8 correctly"""
    out = check50.run("cargo run").stdin("8").stdout()
    check_pyramid(out, open("8.txt").read())

@check50.check(compiles)
def test9():
    """rejects a height of 9, and then accepts a height of 2"""
    out = check50.run("cargo run").stdin("9").reject().stdin("2").stdout()
    check_pyramid(out, open("2.txt").read())

@check50.check(compiles)
def test_reject_foo():
    """rejects a non-numeric height of "foo" """
    check50.run("cargo run").stdin("foo").reject()

@check50.check(compiles)
def test_reject_empty():
    """rejects a non-numeric height of "" """
    check50.run("cargo run").stdin("").reject()


def check_pyramid(output, correct):
    if output == correct:
        return

    output = [line for line in output.splitlines() if line != ""]
    correct = correct.splitlines()

    help = None
    if len(output) == len(correct):
        if all(ol.rstrip() == cl for ol, cl in zip(output, correct)):
            help = "did you add too much trailing whitespace to the end of your pyramid?"
        elif all(ol[1:] == cl for ol, cl in zip(output, correct)):
            help = "are you printing an additional character at the beginning of each line?"

    raise check50.Mismatch(correct, output, help=help)
