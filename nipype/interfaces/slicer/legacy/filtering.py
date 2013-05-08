# -*- coding: utf8 -*- 
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import CommandLine, CommandLineInputSpec, SEMLikeCommandLine, TraitedSpec, File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath
import os


class OtsuThresholdImageFilterInputSpec(CommandLineInputSpec):
    insideValue = traits.Int(desc="The value assigned to pixels that are inside the computed threshold", argstr="--insideValue %d")
    outsideValue = traits.Int(desc="The value assigned to pixels that are outside the computed threshold", argstr="--outsideValue %d")
    numberOfBins = traits.Int(desc="This is an advanced parameter. The number of bins in the histogram used to model the probability mass function of the two intensity distributions. Small numbers of bins may result in a more conservative threshold. The default should suffice for most applications. Experimentation is the only way to see the effect of varying this parameter.", argstr="--numberOfBins %d")
    inputVolume = File(position=-2, desc="Input volume to be filtered", exists=True, argstr="%s")
    outputVolume = traits.Either(traits.Bool, File(), position=-1, hash_files=False, desc="Output filtered", argstr="%s")


class OtsuThresholdImageFilterOutputSpec(TraitedSpec):
    outputVolume = File(position=-1, desc="Output filtered", exists=True)


class OtsuThresholdImageFilter(SEMLikeCommandLine):
    """title: Otsu Threshold Image Filter

category: Legacy.Filtering

description: This filter creates a binary thresholded image that separates an image into foreground and background components. The filter calculates the optimum threshold separating those two classes so that their combined spread (intra-class variance) is minimal (see http://en.wikipedia.org/wiki/Otsu%27s_method).  Then the filter applies that threshold to the input image using the itkBinaryThresholdImageFilter. The numberOfHistogram bins can be set for the Otsu Calculator. The insideValue and outsideValue can be set for the BinaryThresholdImageFilter.  The filter produces a labeled volume.

The original reference is: 

N.Otsu, ‘‘A threshold selection method from gray level histograms,’’ IEEE Trans.Syst.ManCybern.SMC-9,62–66 1979.

version: 0.1.0.$Revision: 19608 $(alpha)

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/OtsuThresholdImageFilter

contributor: Bill Lorensen (GE)

acknowledgements: This command module was derived from Insight/Examples (copyright) Insight Software Consortium

"""

    input_spec = OtsuThresholdImageFilterInputSpec
    output_spec = OtsuThresholdImageFilterOutputSpec
    _cmd = "OtsuThresholdImageFilter "
    _outputs_filenames = {'outputVolume':'outputVolume.nii'}


class ResampleScalarVolumeInputSpec(CommandLineInputSpec):
    spacing = InputMultiPath(traits.Float, desc="Spacing along each dimension (0 means use input spacing)", sep=",", argstr="--spacing %s")
    interpolation = traits.Enum("linear", "nearestNeighbor", "bspline", "hamming", "cosine", "welch", "lanczos", "blackman", desc="Sampling algorithm (linear, nearest neighbor, bspline(cubic)  or windowed sinc). There are several sinc algorithms available as described in the following publication: Erik H. W. Meijering, Wiro J. Niessen, Josien P. W. Pluim, Max A. Viergever: Quantitative Comparison of Sinc-Approximating Kernels for Medical Image Interpolation. MICCAI 1999, pp. 210-217. Each window has a radius of 3;", argstr="--interpolation %s")
    InputVolume = File(position=-2, desc="Input volume to be resampled", exists=True, argstr="%s")
    OutputVolume = traits.Either(traits.Bool, File(), position=-1, hash_files=False, desc="Resampled Volume", argstr="%s")


class ResampleScalarVolumeOutputSpec(TraitedSpec):
    OutputVolume = File(position=-1, desc="Resampled Volume", exists=True)


class ResampleScalarVolume(SEMLikeCommandLine):
    """title: Resample Scalar Volume

category: Legacy.Filtering

description: Resampling an image is an important task in image analysis. It is especially important in the frame of image registration. This module implements image resampling through the use of itk Transforms. This module uses an Identity Transform. The resampling is controlled by the Output Spacing. "Resampling" is performed in space coordinates, not pixel/grid coordinates. It is quite important to ensure that image spacing is properly set on the images involved. The interpolator is required since the mapping from one space to the other will often require evaluation of the intensity of the image at non-grid positions. Several interpolators are available: linear, nearest neighbor, bspline and five flavors of sinc. The sinc interpolators, although more precise, are much slower than the linear and nearest neighbor interpolator. To resample label volumnes, nearest neighbor interpolation should be used exclusively.

version: 0.1.0.$Revision: 20594 $(alpha)

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/ResampleVolume

contributor: Bill Lorensen (GE)

acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.

"""

    input_spec = ResampleScalarVolumeInputSpec
    output_spec = ResampleScalarVolumeOutputSpec
    _cmd = "ResampleScalarVolume "
    _outputs_filenames = {'OutputVolume':'OutputVolume.nii'}
