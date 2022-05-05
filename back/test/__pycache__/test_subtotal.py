from src.main import calculated_subtotal

def test_if_subtotal_is_correct():
    mydict =  {'product': 'pan', 'cuantity': 1, 'value': 1.2}
    expect =   1.2
    result =  calculated_subtotal(mydict)
    assert expect == result