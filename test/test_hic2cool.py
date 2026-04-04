import pytest

from bioconvert.hic2cool import HIC2COOL
from bioconvert import TempFile

from . import test_dir


@pytest.mark.parametrize("method", HIC2COOL.available_methods)
def test_conv(method):
    infile = f"{test_dir}/data/hic/test.hic"
    with TempFile(suffix=".cool") as tempfile:
        convert = HIC2COOL(infile, tempfile.name)
        convert(method=method)
