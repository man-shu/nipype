# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..dcm2nii import Dcm2niix


def test_Dcm2niix_inputs():
    input_map = dict(
        anon_bids=dict(
            argstr="-ba",
            requires=["bids_format"],
        ),
        args=dict(
            argstr="%s",
        ),
        bids_format=dict(
            argstr="-b",
            usedefault=True,
        ),
        comment=dict(
            argstr="-c %s",
        ),
        compress=dict(
            argstr="-z %s",
            usedefault=True,
        ),
        compression=dict(
            argstr="-%d",
        ),
        crop=dict(
            argstr="-x",
            usedefault=True,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        has_private=dict(
            argstr="-t",
            usedefault=True,
        ),
        ignore_deriv=dict(
            argstr="-i",
        ),
        merge_imgs=dict(
            argstr="-m %d",
            usedefault=True,
        ),
        out_filename=dict(
            argstr="-f %s",
        ),
        output_dir=dict(
            argstr="-o %s",
            usedefault=True,
        ),
        philips_float=dict(
            argstr="-p",
        ),
        series_numbers=dict(
            argstr="-n %s...",
        ),
        single_file=dict(
            argstr="-s",
            usedefault=True,
        ),
        source_dir=dict(
            argstr="%s",
            mandatory=True,
            position=-1,
            xor=["source_names"],
        ),
        source_names=dict(
            argstr="%s",
            copyfile=False,
            mandatory=True,
            position=-1,
            xor=["source_dir"],
        ),
        to_nrrd=dict(
            argstr="-e",
        ),
        verbose=dict(
            argstr="-v",
            usedefault=True,
        ),
    )
    inputs = Dcm2niix.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Dcm2niix_outputs():
    output_map = dict(
        bids=dict(),
        bvals=dict(),
        bvecs=dict(),
        converted_files=dict(),
    )
    outputs = Dcm2niix.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
