# <img alt="NumPy" src="https://cdn.rawgit.com/numpy/numpy/master/branding/icons/numpylogo.svg" height="60">

[![Travis](https://img.shields.io/travis/numpy/numpy/master.svg?label=Travis%20CI)](
    https://travis-ci.org/numpy/numpy)
[![AppVeyor](https://img.shields.io/appveyor/ci/charris/numpy/master.svg?label=AppVeyor)](
    https://ci.appveyor.com/project/charris/numpy)
[![Azure](https://dev.azure.com/numpy/numpy/_apis/build/status/azure-pipeline%20numpy.numpy)](
    https://dev.azure.com/numpy/numpy/_build/latest?definitionId=5)
[![codecov](https://codecov.io/gh/numpy/numpy/branch/master/graph/badge.svg)](
    https://codecov.io/gh/numpy/numpy)

NumPy is the fundamental package needed for scientific computing with Python.

- **Website (including documentation):** https://www.numpy.org
- **Mailing list:** https://mail.python.org/mailman/listinfo/numpy-discussion
- **Source:** https://github.com/numpy/numpy
- **Bug reports:** https://github.com/numpy/numpy/issues

It provides:

- a powerful N-dimensional array object
- sophisticated (broadcasting) functions
- tools for integrating C/C++ and Fortran code
- useful linear algebra, Fourier transform, and random number capabilities

Testing:

- NumPy versions &ge; 1.15 require `pytest`
- NumPy versions &lt; 1.15 require `nose`

Tests can then be run after installation with:

    python -c 'import numpy; numpy.test()'

[![Powered by NumFOCUS](https://img.shields.io/badge/powered%20by-NumFOCUS-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](https://numfocus.org)

## Part 1: Complexity measurement

Ten python functions with the highest _cyclomatic complexity_ (CNN) according to lizard:

```
================================================
  NLOC    CCN   token  PARAM  length  location
------------------------------------------------
     121     50    960      2     126 buildcallback@452-577@numpy/numpy/f2py/cb_rules.py
     148     53   1096      3     238 _get_multi_index@801-1038@numpy/numpy/core/tests/test_indexing.py
     114     55    849      5     119 vars2fortran@3125-3243@numpy/numpy/f2py/crackfortran.py
     138     55    749      1     139 scaninputline@176-314@numpy/numpy/f2py/f2py2e.py
     143     55   1295      3     148 getarrlen@2167-2314@numpy/numpy/f2py/crackfortran.py
     147     58   1177      0     169 run_compile@487-655@numpy/numpy/f2py/f2py2e.py
     191     58   1158      3     206 readfortrancode@330-535@numpy/numpy/f2py/crackfortran.py
     140     65   1172      4     142 updatevars@1536-1677@numpy/numpy/f2py/crackfortran.py
     335    162   3021      1     347 analyzevars@2524-2870@numpy/numpy/f2py/crackfortran.py
     527    176   3988      3     545 analyzeline@903-1447@numpy/numpy/f2py/crackfortran.py
```
