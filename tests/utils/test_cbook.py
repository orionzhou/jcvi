import os.path as op
import pytest


@pytest.mark.parametrize(
    "input,output",
    [("AT5G54690.2", "AT5G54690"), ("evm.test.1", "evm.test.1")],
)
def test_gene_name(input, output):
    from jcvi.utils.cbook import gene_name

    assert gene_name(input) == output


@pytest.mark.parametrize(
    "seqid,sep,stdpf,output",
    [
        ("chr1_random", ["-"], False, ("chr", "1", "_random")),
        ("chr1_random", ["-"], True, ("C", "1", "_random")),
        ("AmTr_v1.0_scaffold00001", ["-"], False, ("AmTr_v1.0_scaffold", "00001", "")),
        ("AmTr_v1.0_scaffold00001", [], True, ("Sca", "00001", "")),
        ("PDK_30s1055861", [], True, ("C", "1055861", "")),
        ("PDK_30s1055861", ["-"], False, ("PDK_30s", "1055861", "")),
        ("AC235758.1", ["-"], False, ("AC", "235758.1", "")),
    ],
)
def test_seqid_parse(seqid, sep, stdpf, output):
    from jcvi.utils.cbook import seqid_parse

    assert seqid_parse(seqid, sep, stdpf) == output


def test_depends():
    from jcvi.apps.base import cleanup
    from jcvi.utils.cbook import depends

    @depends
    def func1(infile="a", outfile="b"):
        assert op.exists(infile)
        with open(outfile, "w"):
            pass

    with open("a", "w"):
        pass
    func1(infile="a", outfile="b")
    assert op.exists("b")
    cleanup("a", "b")
