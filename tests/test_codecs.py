import pytest
import sys
import tools.codecs
from StringIO import StringIO


@pytest.fixture
def c():
    return tools.codecs.Codecs()


def test_base64_enc(c):
    out = StringIO()
    sys.stdout = out

    c.do_b64('enc test string 1')

    output = out.getvalue().strip()
    assert output == 'dGVzdCBzdHJpbmcgMQ=='
    assert output != 'test string 1'

    sys.stdout.seek(0)
    c.do_b64('enc ')
    output = out.getvalue().strip()
    assert output == 'Usage: b64 [dec|enc] <string>'


def test_base64_dec(c):
    out = StringIO()
    sys.stdout = out

    c.do_b64('dec dGVzdGluZyBkZWNvZGluZw==')

    output = out.getvalue().strip()
    assert output == 'testing decoding'

    sys.stdout.seek(0)
    c.do_b64('dec ')
    output = out.getvalue().strip()
    assert output == 'Usage: b64 [dec|enc] <string>'
