from __future__ import division, absolute_import, print_function

from distutils.dist import Distribution

from numpy.distutils.command.build_src import build_src
from numpy.testing import assert_

class TestBuildSrc(object):
    
    def test_f2py_opts(self):
        """
        Test that finalize_options correctly handles f2py_opts.
        """

        distribution = Distribution()
        instance = build_src(distribution)
        instance.initialize_options()

        instance.f2py_opts = '--2d-numpy --g3-numpy'

        instance.finalize_options()

        assert_(instance.f2py_opts == ['--2d-numpy', '--g3-numpy'])
