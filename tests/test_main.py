import FHParser.parser as myCode

def test_valid_CIK():
    #CIK need 10 digits
    valid_CIK = '0123456789'
    assert True == myCode.verify_CIK(valid_CIK)

def test_invalid_CIK():
    #CIK with less than 10 digits
    invalid_CIK = '0'
    assert False == myCode.verify_CIK(invalid_CIK)

    #CIK with more than 10 digits
    invalid_CIK = '01234567890'
    assert False == myCode.verify_CIK(invalid_CIK)

def test_valid_Ticker():
    #valid ticker needs 5 letters, ending with an X
    valid_ticker = 'ABCDX'
    assert True == myCode.verify_CIK(valid_ticker)

def test_invalid_Ticker():
    #Ticker with 5 letters, without an X
    invalid_ticker = 'ABCDE'
    assert False == myCode.verify_CIK(invalid_ticker)

    #Ticker with less than 5 letters
    invalid_ticker = 'abcX'
    assert False == myCode.verify_CIK(invalid_ticker)

    #Ticker with more than 5 letters
    invalid_ticker = 'abcdeX'
    assert False == myCode.verify_CIK(invalid_ticker)

def test_valid_CIK_with_results():
    valid_CIK = '0001166559'
    result = None
    try:
        result = next(myCode.find_13f_archive(valid_CIK))
    except StopIteration:
        result = None
    finally:
        assert None != result

def test_valid_CIK_no_results():
    valid_CIK = 'NGINX'
    result = None
    try:
        result = next(myCode.find_13f_archive(valid_CIK))
    except StopIteration:
        result = None
    finally:
        assert None == result

# Since actual can't be called without a match to a 13F, I think I'm safe.
def test_valid_CIK_archive():
    valid_CIK = '0001166559'
    archive = next(myCode.find_13f_archive(valid_CIK))
    assert None != myCode.find_13f_actual(archive)
