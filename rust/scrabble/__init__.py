import check50
import check50.rust

@check50.check()
def exists():
    """main.rs exists"""
    check50.exists("src/main.rs")

@check50.check(exists)
def compiles():
    """min.rs compiles"""
    check50.rust.compile()

@check50.check(compiles)
def tie_letter_case():
    """handles letter cases correctly"""
    check50.run("cargo run").stdin("LETTERCASE").stdin("lettercase").stdout("[Tt]ie!?", "Tie!").exit(0)

@check50.check(compiles)
def tie_punctuation():
    """handles punctuation correctly"""
    check50.run("cargo run").stdin("Punctuation!?!?").stdin("punctuation").stdout("[Tt]ie!?", "Tie!").exit(0)

@check50.check(compiles)
def test1():
    """correctly identifies 'Question?' and 'Question!' as a tie"""
    check50.run("cargo run").stdin("Question?").stdin("Question!").stdout("[Tt]ie!?", "Tie!").exit(0)

@check50.check(compiles)
def test2():
    """correctly identifies 'drawing' and 'illustration' as a tie"""
    check50.run("cargo run").stdin("drawing").stdin("illustration").stdout("[Tt]ie!?", "Tie!").exit(0)

@check50.check(compiles)
def test3():
    """correctly identifies 'hai!' as winner over 'Oh,'"""
    check50.run("cargo run").stdin("Oh,").stdin("hai!").stdout("[Pp]layer 2 [Ww]ins!?", "Player 2 wins!").exit(0)

@check50.check(compiles)
def test4():
    """correctly identifies 'COMPUTER' as winner over 'science'"""
    check50.run("cargo run").stdin("COMPUTER").stdin("science").stdout("[Pp]layer 1 [Ww]ins!?", "Player 1 wins!").exit(0)

@check50.check(compiles)
def test5():
    """correctly identifies 'Scrabble' as winner over 'wiNNeR'"""
    check50.run("cargo run").stdin("Scrabble").stdin("wiNNeR").stdout("[Pp]layer 1 [Ww]ins!?", "Player 1 wins!").exit(0)

@check50.check(compiles)
def test6():
    """correctly identifies 'pig' as winner over 'dog'"""
    check50.run("cargo run").stdin("pig").stdin("dog").stdout("[Pp]layer 1 [Ww]ins!?", "Player 1 wins!").exit(0)

@check50.check(compiles)
def complex_case():
    """correctly identifies 'Skating!' as winner over 'figure?'"""
    check50.run("cargo run").stdin("figure?").stdin("Skating!").stdout("[Pp]layer 2 [Ww]ins!?", "Player 2 wins!").exit(0)

