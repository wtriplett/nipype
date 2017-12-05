# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import Normalize12


def test_Normalize12_inputs():
    input_map = dict(affine_regularization_type=dict(field='eoptions.affreg',
    ),
    apply_to_files=dict(copyfile=True,
    field='subj.resample',
    ),
    bias_fwhm=dict(field='eoptions.biasfwhm',
    ),
    bias_regularization=dict(field='eoptions.biasreg',
    ),
    deformation_file=dict(copyfile=False,
    field='subj.def',
    mandatory=True,
    xor=['image_to_align', 'tpm'],
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    image_to_align=dict(copyfile=True,
    field='subj.vol',
    mandatory=True,
    xor=['deformation_file'],
    ),
    jobtype=dict(usedefault=True,
    ),
    matlab_cmd=dict(),
    mfile=dict(usedefault=True,
    ),
    out_prefix=dict(field='woptions.prefix',
    usedefault=True,
    ),
    paths=dict(),
    sampling_distance=dict(field='eoptions.samp',
    ),
    smoothness=dict(field='eoptions.fwhm',
    ),
    tpm=dict(copyfile=False,
    field='eoptions.tpm',
    xor=['deformation_file'],
    ),
    use_mcr=dict(),
    use_v8struct=dict(min_ver='8',
    usedefault=True,
    ),
    warping_regularization=dict(field='eoptions.reg',
    ),
    write_bounding_box=dict(field='woptions.bb',
    ),
    write_interp=dict(field='woptions.interp',
    ),
    write_voxel_sizes=dict(field='woptions.vox',
    ),
    )
    inputs = Normalize12.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Normalize12_outputs():
    output_map = dict(deformation_field=dict(),
    normalized_files=dict(),
    normalized_image=dict(),
    )
    outputs = Normalize12.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
