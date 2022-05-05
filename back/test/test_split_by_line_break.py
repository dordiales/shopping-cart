from src.main import split_counted_by_line_break
from textwrap import dedent


def test_split_line():
    text = dedent(
        """\
        pan|1|1.20
        """
    )
    expect = ["pan|1|1.20"]  
    result = split_counted_by_line_break(text)
    assert expect == result


def test_split_lines():
    text = dedent(
        """\
        pan|1|1.20
        queso|2|3.70
        Leche|12|0.84
        """
    )
    expect = ["pan|1|1.20","queso|2|3.70","Leche|12|0.84"]  
    result = split_counted_by_line_break(text)
    assert expect == result

def test_split_with_spaces():
    text = dedent(
        """\
        carne de tochomosca|1|1.20
        """
    )
    expect = ["carne de tochomosca|1|1.20"]  
    result = split_counted_by_line_break(text)
    assert expect == result