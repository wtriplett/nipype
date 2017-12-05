# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..developer import RandomVol


def test_RandomVol_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    inField=dict(argstr='--inField %s',
    ),
    inLambda=dict(argstr='--inLambda %f',
    ),
    inMaximum=dict(argstr='--inMaximum %d',
    ),
    inMinimum=dict(argstr='--inMinimum %d',
    ),
    inSize=dict(argstr='--inSize %d',
    ),
    inSize2=dict(argstr='--inSize2 %d',
    ),
    inSize3=dict(argstr='--inSize3 %d',
    ),
    inSize4=dict(argstr='--inSize4 %d',
    ),
    inStandard=dict(argstr='--inStandard %d',
    ),
    null=dict(argstr='--null %s',
    ),
    outRand1=dict(argstr='--outRand1 %s',
    hash_files=False,
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    xDefaultMem=dict(argstr='-xDefaultMem %d',
    ),
    xMaxProcess=dict(argstr='-xMaxProcess %d',
    usedefault=True,
    ),
    xPrefExt=dict(argstr='--xPrefExt %s',
    ),
    )
    inputs = RandomVol.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_RandomVol_outputs():
    output_map = dict(outRand1=dict(),
    )
    outputs = RandomVol.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
