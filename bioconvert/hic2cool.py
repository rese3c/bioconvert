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
"""Convert :term:`HIC` format to :term:`COOL` format"""
import colorlog

from bioconvert import ConvBase
from bioconvert.core.decorators import requires

logger = colorlog.getLogger(__name__)

__all__ = ["HIC2COOL"]


class HIC2COOL(ConvBase):
    """Convert :term:`HIC` file to :term:`COOL` file

    Convert a Hi-C contact map in Juicer :term:`HIC` format to the Cooler
    :term:`COOL` format.

    Methods available are based on hic2cool [HIC2COOL]_.

    .. seealso:: :class:`~bioconvert.cool2hic.COOL2HIC`
    """

    #: Default value
    _default_method = "hic2cool"

    def __init__(self, infile, outfile):
        """.. rubric:: constructor

        :param str infile: input :term:`HIC` file
        :param str outfile: output :term:`COOL` file
        """
        super(HIC2COOL, self).__init__(infile, outfile)

    @requires("hic2cool")
    def _method_hic2cool(self, resolution=0, *args, **kwargs):
        """Convert :term:`HIC` to :term:`COOL` using the hic2cool tool.

        When *resolution* is 0 (the default), all available resolutions are
        extracted and saved in a multi-resolution :term:`MCOOL` file.  Pass a
        specific base-pair resolution to obtain a single-resolution
        :term:`COOL` file.

        `hic2cool documentation <https://github.com/4dn-dcic/hic2cool>`_"""
        cmd = "hic2cool convert {infile} {outfile} -r {resolution}".format(
            infile=self.infile,
            outfile=self.outfile,
            resolution=resolution,
        )
        self.execute(cmd)
