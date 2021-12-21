import check50
import check50.rust

@check50.check()
def exists():
    """main.rs exists."""
    check50.exists("src/main.rs")

@check50.check(exists)
def compiles():
    """main.rs compiles."""
    check50.rust.compile()

@check50.check(compiles)
def encrypts_a_as_b():
    """encrypts "a" as "b" using 1 as key"""
    check50.run("cargo run 1").stdin("a").stdout("[Cc]iphertext:\s*b\n", "ciphertext: b\n").exit(0)

@check50.check(compiles)
def encrypts_barfoo_as_yxocll():
    """encrypts "barfoo" as "yxocll" using 23 as key"""
    check50.run("cargo run 23").stdin("barfoo").stdout("[Cc]iphertext:\s*yxocll\n", "ciphertext: yxocll\n").exit(0)

@check50.check(compiles)
def encrypts_BARFOO_as_EDUIRR():
    """encrypts "BARFOO" as "EDUIRR" using 3 as key"""
    check50.run("cargo run 3").stdin("BARFOO").stdout("[Cc]iphertext:\s*EDUIRR\n", "ciphertext: EDUIRR\n").exit(0)

@check50.check(compiles)
def encrypts_BaRFoo_FeVJss():
    """encrypts "BaRFoo" as "FeVJss" using 4 as key"""
    check50.run("cargo run 4").stdin("BaRFoo").stdout("[Cc]iphertext:\s*FeVJss\n", "ciphertext: FeVJss\n").exit(0)

@check50.check(compiles)
def encrypts_barfoo_as_onesbb():
    """encrypts "barfoo" as "onesbb" using 65 as key"""
    check50.run("cargo run 65").stdin("barfoo").stdout("[Cc]iphertext:\s*onesbb\n", "ciphertext: onesbb\n").exit(0)

@check50.check(compiles)
def checks_for_handling_non_alpha():
    """encrypts "world, say hello!" as "iadxp, emk tqxxa!" using 12 as key"""
    check50.run("cargo run 12").stdin("world, say hello!").stdout("[Cc]iphertext:\s*iadxp, emk tqxxa!\n", "ciphertext: iadxp, emk tqxxa!\n").exit(0)

@check50.check(compiles)
def handles_no_argv():
    """handles lack of argv[1]"""
    check50.run("cargo run").exit(1)
    
@check50.check(compiles)
def handles_non_numeric_argv():
    """handles non-numeric key"""
    check50.run("cargo run 2x").exit(1)
    
@check50.check(compiles)
def too_many_args():
    """handles too many arguments"""
    check50.run("cargo run 1 2").exit(1)
