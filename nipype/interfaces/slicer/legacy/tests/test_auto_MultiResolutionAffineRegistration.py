# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..registration import MultiResolutionAffineRegistration


def test_MultiResolutionAffineRegistration_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    fixedImage=dict(argstr='%s',
    position=-2,
    ),
    fixedImageMask=dict(argstr='--fixedImageMask %s',
    ),
    fixedImageROI=dict(argstr='--fixedImageROI %s',
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    metricTolerance=dict(argstr='--metricTolerance %f',
    ),
    movingImage=dict(argstr='%s',
    position=-1,
    ),
    numIterations=dict(argstr='--numIterations %d',
    ),
    numLineIterations=dict(argstr='--numLineIterations %d',
    ),
    resampledImage=dict(argstr='--resampledImage %s',
    hash_files=False,
    ),
    saveTransform=dict(argstr='--saveTransform %s',
    hash_files=False,
    ),
    stepSize=dict(argstr='--stepSize %f',
    ),
    stepTolerance=dict(argstr='--stepTolerance %f',
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    )
    inputs = MultiResolutionAffineRegistration.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_MultiResolutionAffineRegistration_outputs():
    output_map = dict(resampledImage=dict(),
    saveTransform=dict(),
    )
    outputs = MultiResolutionAffineRegistration.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
