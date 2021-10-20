# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


# support
import mdweb


# declaration
class Config(mdweb.shells.command, family="mdweb.cli.config"):
    """
    Display configuration information about this package
    """


    # version info
    @mdweb.export(tip="the version information")
    def version(self, **kwds):
        """
        Print the version of the mdweb package
        """
        # print the version number
        print(f"{mdweb.meta.version}")
        # all done
        return 0


    # configuration
    @mdweb.export(tip="the top level installation directory")
    def prefix(self, **kwds):
        """
        Print the top level installation directory
        """
        # print the installation location
        print(f"{mdweb.prefix}")
        # all done
        return 0


    @mdweb.export(tip="the directory with the executable scripts")
    def path(self, **kwds):
        """
        Print the location of the executable scripts
        """
        # print the path to the bin directory
        print(f"{mdweb.prefix}/bin")
        # all done
        return 0


    @mdweb.export(tip="the directory with the python packages")
    def pythonpath(self, **kwds):
        """
        Print the directory with the python packages
        """
        # print the path to the python package
        print(f"{mdweb.home.parent}")
        # all done
        return 0


    @mdweb.export(tip="the location of the {mdweb} headers")
    def incpath(self, **kwds):
        """
        Print the locations of the {mdweb} headers
        """
        # print the path to the headers
        print(f"{mdweb.prefix}/include")
        # all done
        return 0


    @mdweb.export(tip="the location of the {mdweb} libraries")
    def libpath(self, **kwds):
        """
        Print the locations of the {mdweb} libraries
        """
        # print the path to the libraries
        print(f"{mdweb.prefix}/lib")
        # all done
        return 0


# end of file
