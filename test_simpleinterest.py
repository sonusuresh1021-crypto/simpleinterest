from simple_interest import simple_interest

def test_zero_princpal():
    assert simple_interest(0,2,1) == 0

def test_zero_rate():
    assert simple_interest(10000,0,2) == 0    

def test_decimal_values():
    assert simple_interest(5000,4.5,2) == 450