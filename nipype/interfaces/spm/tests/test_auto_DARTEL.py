# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import DARTEL


def test_DARTEL_inputs():
    input_map = dict(ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    image_files=dict(copyfile=False,
    field='warp.images',
    mandatory=True,
    ),
    iteration_parameters=dict(field='warp.settings.param',
    ),
    matlab_cmd=dict(),
    mfile=dict(usedefault=True,
    ),
    optimization_parameters=dict(field='warp.settings.optim',
    ),
    paths=dict(),
    regularization_form=dict(field='warp.settings.rform',
    ),
    template_prefix=dict(field='warp.settings.template',
    usedefault=True,
    ),
    use_mcr=dict(),
    use_v8struct=dict(min_ver='8',
    usedefault=True,
    ),
    )
    inputs = DARTEL.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_DARTEL_outputs():
    output_map = dict(dartel_flow_fields=dict(),
    final_template_file=dict(),
    template_files=dict(),
    )
    outputs = DARTEL.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
