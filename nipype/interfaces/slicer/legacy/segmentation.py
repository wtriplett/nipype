# -*- coding: utf-8 -*-
# -*- coding: utf8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import CommandLine, CommandLineInputSpec, SEMLikeCommandLine, TraitedSpec, File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath
import os


class OtsuThresholdSegmentationInputSpec(CommandLineInputSpec):
    brightObjects = traits.Bool(
        desc=
        "Segmenting bright objects on a dark background or dark objects on a bright background.",
        argstr="--brightObjects ")
    numberOfBins = traits.Int(
        desc=
        "This is an advanced parameter. The number of bins in the histogram used to model the probability mass function of the two intensity distributions. Small numbers of bins may result in a more conservative threshold. The default should suffice for most applications. Experimentation is the only way to see the effect of varying this parameter.",
        argstr="--numberOfBins %d")
    faceConnected = traits.Bool(
        desc=
        "This is an advanced parameter. Adjacent voxels are face connected. This affects the connected component algorithm. If this parameter is false, more regions are likely to be identified.",
        argstr="--faceConnected ")
    minimumObjectSize = traits.Int(
        desc=
        "Minimum size of object to retain. This parameter can be used to get rid of small regions in noisy images.",
        argstr="--minimumObjectSize %d")
    inputVolume = File(
        position=-2,
        desc="Input volume to be segmented",
        exists=True,
        argstr="%s")
    outputVolume = traits.Either(
        traits.Bool,
        File(),
        position=-1,
        hash_files=False,
        desc="Output filtered",
        argstr="%s")


class OtsuThresholdSegmentationOutputSpec(TraitedSpec):
    outputVolume = File(position=-1, desc="Output filtered", exists=True)


class OtsuThresholdSegmentation(SEMLikeCommandLine):
    """title: Otsu Threshold Segmentation

category: Legacy.Segmentation

description: This filter creates a labeled image from a grayscale image. First, it calculates an optimal threshold that separates the image into foreground and background. This threshold separates those two classes so that their intra-class variance is minimal (see http://en.wikipedia.org/wiki/Otsu%27s_method). Then the filter runs a connected component algorithm to generate unique labels for each connected region of the foreground. Finally, the resulting image is relabeled to provide consecutive numbering.

version: 1.0

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/OtsuThresholdSegmentation

contributor: Bill Lorensen (GE)

acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.

"""

    input_spec = OtsuThresholdSegmentationInputSpec
    output_spec = OtsuThresholdSegmentationOutputSpec
    _cmd = "OtsuThresholdSegmentation "
    _outputs_filenames = {'outputVolume': 'outputVolume.nii'}
