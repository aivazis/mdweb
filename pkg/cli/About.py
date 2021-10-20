# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


# externals
import mdweb


# declaration
class About(mdweb.shells.command, family='mdweb.cli.about'):
    """
    Display information about this application
    """


    @mdweb.export(tip="print the copyright note")
    def copyright(self, plexus, **kwds):
        """
        Print the copyright note of the mdweb package
        """
        # show the copyright note
        plexus.info.log(mdweb.meta.copyright)
        # all done
        return


    @mdweb.export(tip="print out the acknowledgments")
    def credits(self, plexus, **kwds):
        """
        Print out the license and terms of use of the mdweb package
        """
        # make some space
        plexus.info.log(mdweb.meta.header)
        # all done
        return


    @mdweb.export(tip="print out the license and terms of use")
    def license(self, plexus, **kwds):
        """
        Print out the license and terms of use of the mdweb package
        """
        # make some space
        plexus.info.log(mdweb.meta.license)
        # all done
        return


    @mdweb.export(tip="print the version number")
    def version(self, plexus, **kwds):
        """
        Print the version of the mdweb package
        """
        # make some space
        plexus.info.log(mdweb.meta.header)
        # all done
        return


# end of file
