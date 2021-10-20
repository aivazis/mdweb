# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved

# bash completion script for mdweb
function _mdweb() {
    # get the partial command line
    local line=${COMP_LINE}
    local word=${COMP_WORDS[COMP_CWORD]}
    # ask mdweb to provide guesses
    COMPREPLY=($(mdweb complete --word="${word}" --line="${line}"))
}

# register the hook
complete -F _mdweb mdweb

# end of file
