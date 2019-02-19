import pytest
import os

import platform

from numpy.testing import assert_, assert_equal
from numpy.distutils import ccompiler
from distutils.unixccompiler import UnixCCompiler

class MockCompiler(UnixCCompiler):
    """A modified Intel compiler compatible with a GCC-built Python."""
    compiler_type = 'intel'
    cc_exe = 'icc'
    cc_args = 'fPIC'

    def __init__(self, compiler, compiler_cxx):
        UnixCCompiler.__init__(self, 0, 0, 0)

        self.cc_exe = compiler

        if platform.system() == 'Darwin':
           shared_flag = '-Wl,-undefined,dynamic_lookup'
        else:
           shared_flag = '-shared'

        self.set_executables(compiler=compiler,
                            compiler_so=compiler,
                            compiler_cxx=compiler_cxx,
                            archiver='xiar' + ' cru',
                            linker_exe=compiler + ' -shared-intel',
                            linker_so=compiler + ' ' + shared_flag +
                            ' -shared-intel')


def test_CCompiler_customize_need_cxx_true_gcc():
    compiler_str = 'gcc -Wstrict-prototypes -someOtherParam'
    compiler = MockCompiler(compiler_str, compiler_str)
    compiler.customize(None, True)
    assert_equal(' '.join(compiler.compiler_cxx), compiler_str)
    assert_equal(' '.join(compiler.compiler_so), "gcc -someOtherParam")

def test_CCompiler_customize_need_cxx_true_gcc_no_cxx():
    compiler_str = 'gcc -Wstrict-prototypes -someOtherParam'
    compiler = MockCompiler(compiler_str, None)
    compiler.customize(None, True)
    assert_equal(' '.join(compiler.compiler_cxx), "g++ -Wstrict-prototypes -someOtherParam")
    assert_equal(' '.join(compiler.compiler_so), "gcc -someOtherParam")


def test_CCompiler_customize_need_cxx_true_non_gcc():
    compiler_str = 'clang -Wstrict-prototypes -someOtherParam'
    compiler = MockCompiler(compiler_str, compiler_str)
    compiler.customize(None, True)
    assert_equal(' '.join(compiler.compiler_cxx), "clang -Wstrict-prototypes -someOtherParam")
    assert_equal(' '.join(compiler.compiler_so), "clang -someOtherParam")

