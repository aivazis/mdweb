# -*- Makefile -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


# mdweb consists of a python package
mdweb.packages := mdweb.pkg
# libraries
mdweb.libraries := 
# python extensions
mdweb.extensions :=
# a ux bundle
mdweb.webpack := mdweb.ux
# and some tests
mdweb.tests := mdweb.pkg.tests


# load the packages
include $(mdweb.packages)
# the libraries
include $(mdweb.libraries)
# the extensions
include $(mdweb.extensions)
# the ux
include $(mdweb.webpack)
# and the test suites
include $(mdweb.tests)


# end of file
