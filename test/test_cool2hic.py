import os

import pytest

from bioconvert.cool2hic import COOL2HIC
from bioconvert import TempFile

from . import test_dir

_cool_infile = f"{test_dir}/data/cool/test.cool"


@pytest.mark.parametrize("method", COOL2HIC.available_methods)
@pytest.mark.skipif(not os.path.exists(_cool_infile), reason="test data not available")
def test_conv(method):
    with TempFile(suffix=".hic") as tempfile:
        convert = COOL2HIC(_cool_infile, tempfile.name)
        convert(method=method)
        assert os.path.exists(tempfile.name)
        assert os.path.getsize(tempfile.name) > 0
