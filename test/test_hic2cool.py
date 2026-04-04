import os

import pytest

from bioconvert.hic2cool import HIC2COOL
from bioconvert import TempFile

from . import test_dir

_hic_infile = f"{test_dir}/data/hic/test.hic"


@pytest.mark.parametrize("method", HIC2COOL.available_methods)
@pytest.mark.skipif(not os.path.exists(_hic_infile), reason="test data not available")
def test_conv(method):
    with TempFile(suffix=".cool") as tempfile:
        convert = HIC2COOL(_hic_infile, tempfile.name)
        convert(method=method)
        assert os.path.exists(tempfile.name)
        assert os.path.getsize(tempfile.name) > 0
