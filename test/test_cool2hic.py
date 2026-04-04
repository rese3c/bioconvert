import pytest

from bioconvert.cool2hic import COOL2HIC
from bioconvert import TempFile

from . import test_dir


@pytest.mark.parametrize("method", COOL2HIC.available_methods)
def test_conv(method):
    infile = f"{test_dir}/data/cool/test.cool"
    with TempFile(suffix=".hic") as tempfile:
        convert = COOL2HIC(infile, tempfile.name)
        convert(method=method)
