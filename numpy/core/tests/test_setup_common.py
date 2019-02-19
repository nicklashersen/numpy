from __future__ import division, absolute_import, print_function

import pytest

from numpy.core.setup_common import long_double_representation
from numpy.testing import assert_

class TestSetupCommon(object):

    def test_long_double_representation_value_error(self):
        """
        Test that an invalid input gives a correct ValueError.
        """

        with pytest.raises(ValueError) as excinfo:
            long_double_representation([])

        assert_(str(excinfo.value) == 'Could not lock sequences (None)')

    def test_long_double_representation_intel_extended_12b(self):
        """
        Test that a valid INTEL_EXTENDED_12B input gives the correct return.
        """

        lines = ['0 000 000 000 000 001 043 105 147 211 253 315 357',
                 '1 000 000 000 000 240 242 171 353 031 300 000 000',
                 '2 376 334 272 230 166 124 062 020']

        return_value = long_double_representation(lines)

        assert_(return_value == 'INTEL_EXTENDED_12_BYTES_LE')
