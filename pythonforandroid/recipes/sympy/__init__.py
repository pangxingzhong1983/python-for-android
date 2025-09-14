from pythonforandroid.recipe import PyProjectRecipe


class SympyRecipe(PyProjectRecipe):

    version = '1.14.0'
    url = 'https://github.com/sympy/sympy/archive/refs/tags/{version}.zip'
    depends = ['mpmath']
    hostpython_prerequisites = ['setuptools', 'build']
    call_hostpython_via_targetpython = False
    install_in_hostpython = True


recipe = SympyRecipe()
