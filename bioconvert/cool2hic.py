###########################################################################
# Bioconvert is a project to facilitate the interconversion               #
# of life science data from one format to another.                        #
#                                                                         #
# Copyright © 2018-2022  Institut Pasteur, Paris and CNRS.                #
#                                                                         #
# bioconvert is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by    #
# the Free Software Foundation, either version 3 of the License, or       #
# (at your option) any later version.                                     #
#                                                                         #
# bioconvert is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of          #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
# GNU General Public License for more details.                            #
#                                                                         #
# You should have received a copy of the GNU General Public License       #
# along with this program (COPYING file).                                 #
# If not, see <http://www.gnu.org/licenses/>.                             #
#                                                                         #
# Repository: https://github.com/bioconvert/bioconvert                    #
# Documentation: http://bioconvert.readthedocs.io                         #
###########################################################################
"""Convert :term:`COOL` format to :term:`HIC` format"""
import colorlog

from bioconvert import ConvBase
from bioconvert.core.decorators import requires

logger = colorlog.getLogger(__name__)

__all__ = ["COOL2HIC"]


class COOL2HIC(ConvBase):
    """Convert :term:`COOL` file to :term:`HIC` file

    Convert a Hi-C contact map in Cooler :term:`COOL` format to the Juicer
    :term:`HIC` format.

    Methods available are based on HiCLift [HICLIFT]_.

    .. seealso:: :class:`~bioconvert.hic2cool.HIC2COOL`
    """

    #: Default value
    _default_method = "hiclift"

    def __init__(self, infile, outfile):
        """.. rubric:: constructor

        :param str infile: input :term:`COOL` file
        :param str outfile: output :term:`HIC` file
        """
        super(COOL2HIC, self).__init__(infile, outfile)

    @requires("HiCLift")
    def _method_hiclift(self, assembly="hg38", *args, **kwargs):
        """Convert :term:`COOL` to :term:`HIC` using HiCLift.

        The *assembly* parameter must match the reference genome used when
        generating the contact map (e.g. ``hg38``, ``hg19``, ``mm10``).
        Both ``--assembly-from`` and ``--assembly-to`` are set to the same
        value so that no coordinate liftover is performed – only the file
        format is converted.

        `HiCLift documentation <https://github.com/XiaoTaoWang/HiCLift>`_"""
        cmd = (
            "HiCLift --input {infile} --input-format cool"
            " --output {outfile} --output-format hic"
            " --assembly-from {assembly} --assembly-to {assembly}"
        ).format(
            infile=self.infile,
            outfile=self.outfile,
            assembly=assembly,
        )
        self.execute(cmd)
