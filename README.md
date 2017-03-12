# nbimporter
Import IPython Notebooks as modules (with Jupyter v4).

## Origin
This is a modified version of code originally from
https://github.com/adrn/ipython/blob/master/examples/Notebook/Importing%20Notebooks.ipynb
Check out that notebook for full documentation and to understand the background. 

## Installation
`pip install nbimporter`

## Usage
**Notebook foo.ipynb:**

In[1]:
```python
def a(): 
    print("Hello World!")
```

**Notebook bar.ipynb:**

In[1]:
```python
import nbimporter
from foo import a #import from notebook

a()
```

Out[1]:
```
Hello World!
```

## Options

Importing from a notebook is different from a module: because one
typically keeps many computations and tests besides exportable defs,
here we only run code which either defines a function or a class, or
imports code from other modules and notebooks. This behaviour can be
disabled by setting `nbimporter.options['only_defs'] = False`.

Furthermore, in order to provide per-notebook initialisation, if a
special function `__init__()` is defined in the notebook, it will be
executed the first time an import statement is. This behaviour can be
disabled by setting `nbimporter.options['run_init'] = False`.

Finally, you can set the encoding of the notebooks with
`nbimporter.options['encoding']`. The default is `'utf-8'`.
