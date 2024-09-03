""" JupyterLab LaTex : live LaTeX editing for JupyterLab """

from traitlets import Unicode, CaselessStrEnum, Integer, Bool, List
from traitlets.config import Configurable

class LatexConfig(Configurable):
    """
    A Configurable that declares the configuration options
    for the LatexHandler.
    """
    latex_command = Unicode('xelatex', config=True,
        help='The LaTeX command to use when compiling ".tex" files.')
    latex_options = List(["-interaction=nonstopmode",
                          "-halt-on-error", 
                          "-file-line-error",
                          "{synctex_flag}",
                          "{escape_flag}"],
        config=True,
        help='The options for LaTeX command.')

    bib_command = Unicode('bibtex', config=True,
        help='The BibTeX command to use when compiling ".tex" files.')
    bib_options = List([], config=True,
        help='The options for LaTeX command.')

    synctex_command = Unicode('synctex', config=True,
        help='The synctex command to use when syncronizing between .tex and .pdf files.')
    shell_escape = CaselessStrEnum(['restricted', 'allow', 'disallow'],
        default_value='restricted', config=True,
        help='Whether to allow shell escapes '+\
        '(and by extension, arbitrary code execution). '+\
        'Can be "restricted", for restricted shell escapes, '+\
        '"allow", to allow all shell escapes, or "disallow", '+\
        'to disallow all shell escapes')
    run_times = Integer(default_value=1, config=True,
        help='How many times to compile the ".tex" files.')
    cleanup = Bool(default_value=True, config=True,
        help='Whether to clean up ".out/.aux" files or not.')

    dvipdf_command = CaselessStrEnum(['none', 'dvipdf', 'dvipdfmx', 'xdvipdfmx'],
        default_value='none', config=True,
        help='The DVIPDF command if you need to run after ".tex" compiling.')
    dvipdf_options = List(['-p', 'a4'], config=True,
        help='The options for DVIPDF command.'+\
             'Note that the filename is append after these options.')
