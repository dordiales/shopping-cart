from src.main import make_list_as_dict

def test_list_as_dict():
    text = [['pan', '1', '1.20']]
    expect = [{'product': 'pan', 'cuantity': 1, 'value': 1.2, 'subtotal': 1.2}]
    result = make_list_as_dict(text)
        
    assert expect == result

def test_lists_as_dict():
    text = [['pan', '1', '1.20'], ['queso', '2', '3.70'], ['Leche', '12', '0.84']]
    expect = [{'product': 'pan', 'cuantity': 1, 'value': 1.2, 'subtotal': 1.2},
              {'product': 'queso', 'cuantity': 2, 'value': 3.7, 'subtotal': 7.4}, 
              {'product': 'Leche', 'cuantity': 12, 'value': 0.84, 'subtotal': 10.08}]
    result = make_list_as_dict(text)
        
    assert expect == result