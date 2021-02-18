import pytest


@pytest.mark.parametrize("program", [
    ("function [out1, out2] = something(x1, x2)\n"
     "    out1=x1^2;\n    out2=(x2+x1)^3;\nend"),
    ("def square_root(x):\n    return (-x**0.5, x**(1/2))"),
    ("s[x_] := (1 + x)*Sqrt[x]")
])
def test_program_balanced(program):
    from brak.brak import Program
    p = Program(program)
    assert p.verify(), \
        "expected True for balanced brackets"


@pytest.mark.parametrize("program, rbrac, line1, pos1, lbrac, line0, pos0", [
    ("function [out1, out2] = something(x1, x2}\n"
     "    out1=x1^2;\n    out2=(x2+x1)^3;\nend", "}",
     0, 40, "(", 0, 33),
    ("def square_root(x]:\n    return (-x**0.5, x**(1/2))",
     "]", 0, 17, "(", 0, 15),
    ("s[x_] := (1 + x]*Sqrt[x]", "]",
     0, 15, "(", 0, 9)
])
def test_program_wrong_bracket(program, lbrac, line0,
                               pos0, rbrac, line1, pos1):
    from brak.brak import Program
    expr = fr"\{lbrac} on line {line0} position {pos0} matched by \{rbrac} "
    f"on line {line1} position {pos1}."
    with pytest.raises(ValueError, match=expr):
        p = Program(program)
        p.verify()


@pytest.mark.parametrize("program, bracket, line_no, pos", [
    ("function [out1, _] = something([[x1, x2]"
     "\n    out1=x1^2;\nend", "[", 0, 31),
    ("def square_root(x):\n    return (-x**0.5, x**1/2))", ")", 1, 28),
    ("s[x_] := (1 + x)*Sqrt[[x]", "[", 0, 21)
])
def test_program_inner_bracket(program, bracket, line_no, pos):
    from brak.brak import Program
    expr = fr"\{bracket} on line {line_no} position {pos} unmatched."
    with pytest.raises(ValueError, match=expr):
        p = Program(program)
        p.verify()


@pytest.mark.parametrize("program, bracket, line_no, pos", [
    ("function [out1, out2] = something(x1, x2)\n"
     "    out1=x1^2;\n""    out2=(x2+x1^3;\nend", "(", 2, 9),
    ("def square_root(x):\n    return (-x**0.5, x**(1/2)", "(", 1, 11),
    ("s[x_] := (1 + x)*Sqrtx]", "]", 0, 22)
])
def test_program_no_bracket(program, bracket, line_no, pos):
    from brak.brak import Program
    expr = fr"\{bracket} on line {line_no} position {pos} unmatched."
    with pytest.raises(ValueError, match=expr):
        p = Program(program)
        p.verify()

