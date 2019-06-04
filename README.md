# nbimporter
Import IPython Notebooks as modules (with Jupyter v4).

## Update 2019-06: I do not recommend any more to use *nbimporter*.
When I created this package some years ago, I still believed that importing 
functions from other notebooks was a good idea for developing and prototyping. 
By now, I have some more years experience in doing data science, and I still 
use Jupyter, however I never import from other notebooks any more. 

### Why?
* **Functions in other notebooks are hard to maintain and hamper reproducibility of other notebooks.** As you use the functions in different projects, you'll want to fix bugs, make performance improvements or re-write it in a more elegant fashion. As soon as you start to fix something in the other notebook, you might break it and your analysis is not reproducible any more. 
* **It is hard to test functions within notebooks**. It is advisable to create a unit test for almost any function. There's no straightforward way to do so within a notebook. Moreover, you might want to edit re-usable code in a powerful IDE that will prevent you from making one or the other mistake. 
* **It is a hack, and doing it properly is *very* easy (see below).** Notebooks are not meant to be imported. This causes issues like [#4](https://github.com/grst/nbimporter/issues/4) and [#5](https://github.com/grst/nbimporter/issues/5). While it is probably totally possible to fix these, doing it properly doesn't cause such problems in the first place. 

### I still want to re-use code (quickly!). What should I do instead?
The **proper** way of doing it is to create a [python module](https://docs.python.org/3/tutorial/modules.html) that contains your functions. 

It is as simple as creating a file in the same directory as your notebooks, e.g. `utils.py` that contains your functions, classes, constants, etc:

**`utils.py`**
```
def my_function(foo):
    return "Hello World!"
```

Congratulations! You created your first python module. Now you can import from it with a single line and zero external dependencies: 

**`notebook.ipynb`**:
```
In [1]: from utils import my_function

In [2]: print(my_function())
Out [2]: "Hello World!"
```

By consequently putting re-usable code into modules, you can use powerful IDEs to develop and debug code, create unit tests, combine multiple modules into shareable packages. In brief, you'll write higher-quality code and re-use more of the code you've written, saving you a lot of time and trouble. 


**Another approach** is to use [jupytext](https://github.com/mwouts/jupytext) that allows you to save jupyter notebooks as plain python scripts from that you can import directly. However that alone does not prevent you from creating code debt.


### Can I still use *nbimporter*?
Sure! If you still believe *nbimporter* fits your workflow best, the
package still works. I won't actively maintain it any longer, but will accept (sensible) 
pull-requests. 

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
special function `__nbinit__()` is defined in the notebook, it will be
executed the first time an import statement is. This behaviour can be
disabled by setting `nbimporter.options['run_nbinit'] = False`.

Finally, you can set the encoding of the notebooks with
`nbimporter.options['encoding']`. The default is `'utf-8'`.
