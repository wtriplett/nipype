# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""Grab documentation from spm."""
import os

from ..interfaces import matlab


def grab_doc(task_name):
    """Grab the SPM documentation for the given SPM task named `task_name`

    Parameters
    ----------
    task_name : string
        Task name for which we are grabbing documentation.  Example
        task names are ``Realign: Estimate & Reslice``, ``Normalise:
        Estimate & Write``.

    See Also
    --------
    spm_flat_config.m : This function can print out all the possible
        task names.

    """

    cmd = matlab.MatlabCommand(resource_monitor=False)
    # We need to tell Matlab where to find our spm_get_doc.m file.
    cwd = os.path.dirname(__file__)
    # Build matlab command
    mcmd = "addpath('%s');spm_get_doc('%s')" % (cwd, task_name)
    cmd.inputs.script_lines = mcmd
    # Run the command and get the documentation out of the result.
    out = cmd.run()
    return _strip_header(out.runtime.stdout)


def _strip_header(doc):
    """Strip Matlab header and splash info off doc.

    Searches for the tag 'NIPYPE' in the doc and returns everyting after that.

    """
    hdr = 'NIPYPE'
    # There's some weird cruft at the end of the docstring, almost looks like
    # the hex for the escape character 0x1b.
    cruft = '\x1b'
    try:
        index = doc.index(hdr)
    except ValueError as e:
        raise IOError('This docstring was not generated by Nipype!\n') from e

    index += len(hdr)
    index += 1
    doc = doc[index:]
    try:
        index = doc.index(cruft)
    except ValueError:
        index = len(doc)
    return doc[:index]
