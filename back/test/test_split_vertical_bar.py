from src.main import split_by_vertical_bar

def test_split_list_by_vertical_bar():
    text = ["pan|1|1.20"] 
    expect = [['pan', '1', '1.20']]
    result = split_by_vertical_bar(text)
    assert  expect == result


def test_split_lists_by_vertical_bar_():
    list = ["pan|1|1.20","queso|2|3.70","Leche|12|0.84"] 
    expect = [['pan', '1', '1.20'], ['queso', '2', '3.70'], ['Leche', '12', '0.84']]
    result = split_by_vertical_bar(list)
    assert  expect == result