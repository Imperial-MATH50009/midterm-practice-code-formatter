import pytest
try:
    from brak.brak import Program
except ImportError:
    pass


def test_program_import():
    from brak.brak import Program


@pytest.mark.parametrize("line_num, line_str", [
    (0, "function [out1, out2] = something(x1, x2)"),
    (1, "    out1=x1^2;"),
    (2, "    out2=(x2+x1)^3;"),
    (3, "end")
])
def test_program_line(line_num, line_str):
    from brak.brak import Program
    p = Program("function [out1, out2] = something(x1, x2)\n"
                "    out1=x1^2;\n    out2=(x2+x1)^3;\nend")
    assert p.line(line_num) == line_str

