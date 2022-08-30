import pkg.Mymodule
pkg.Mymodule.display()
pkg.Mymodule.product()

from pkg import Mymodule
Mymodule.product()

from pkg.Mymodule import display
display()

from pkg.Mymodule import *
display()
product()