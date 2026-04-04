from bioconvert import TempFile, md5
import pytest
from bioconvert.genbank2gff3 import GENBANK2GFF3
from bioconvert.core.registry import Registry

from . import test_dir

# This test fails with wierd pytest error message related
# to io module ?
# FIXME: https://github.com/bioconvert/bioconvert/issues/143
def test_conv():
    infile = f"{test_dir}/data/genbank/biocode.gb"
    outfile = f"{test_dir}/data/GFF3/biocode.gff"

    with TempFile(suffix=".gff") as tempfile:
        converter = GENBANK2GFF3(infile, tempfile.name)
        converter(method="biocode")
        assert md5(tempfile.name) == md5(outfile)


def test_gbff_extension_recognized():
    """Test that .gbff extension is recognized as a valid input format for genbank2gff3."""
    registry = Registry()
    assert (("gbff",), ("gff3",)) in registry._ext_registry, (
        ".gbff extension should be recognized for genbank2gff3 conversion"
    )


def test_conv_cds_without_gene_features():
    """Test that GenBank files with CDS features but no explicit gene features
    produce valid GFF3 output (regression test for GitHub issue: gbff2gff3 empty output)."""
    infile = f"{test_dir}/data/genbank/cds_no_gene.gbk"

    with TempFile(suffix=".gff3") as tempfile:
        converter = GENBANK2GFF3(infile, tempfile.name)
        converter(method="biocode")
        with open(tempfile.name) as fh:
            content = fh.read()

    # Output must contain more than just the GFF3 header
    lines = [l for l in content.splitlines() if l and not l.startswith('#')]
    assert len(lines) > 0, "GFF3 output is empty – CDS features were not converted"
    # Both genes should appear in the output
    assert "GENE001" in content
    assert "GENE002" in content

