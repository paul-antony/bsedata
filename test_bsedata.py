"""

    MIT License

    Copyright (c) 2018 Shrey Dabhi

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

"""

import pytest
from bsedata.bse import BSE

b = BSE(update_codes=True)

@pytest.mark.parametrize("scripCode",['534976','500116','512573'])
def test_getQuote_valid(scripCode):
    assert len(b.getQuote(scripCode)) == 27

def test_getQuote_invalid():
    with pytest.raises(AttributeError):
        assert b.getQuote('513715')

def test_verifyCode_valid():
    assert b.verifyScripCode('534976') == 'V-mart Retail Ltd.'

def test_verifyCode_invalid():
    assert b.verifyScripCode('534980') == None