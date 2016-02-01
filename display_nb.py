# --------------
import io, os
import nbformat
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

from IPython.display import display, HTML

formatter = HtmlFormatter()
lexer = PythonLexer()

# publish the CSS for pygments highlighting
display(HTML("""
<style type='text/css'>
{0}
</style>
""".format(formatter.get_style_defs())
))

def show_notebook(fname):
    """display a short summary of the cells of a notebook"""
    with io.open(fname, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, 4)
    html = []
    for cell in nb.cells:
        html.append("<h4>{0} cell</h4>".format(cell.cell_type))
        if cell.cell_type == 'code':
            html.append(highlight(cell.source, lexer, formatter))
        else:
            html.append("<pre>{0}</pre>".format(cell.source))
    display(HTML('\n'.join(html)))

# Example
#show_notebook(os.path.join("nbimp", "mynotebook.ipynb"))
