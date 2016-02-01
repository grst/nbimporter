# nbimporter
Import IPython Notebooks as modules (with Jupyter v4).

Updated from module collated here:

## Origin
This is a modified version of code originally collated from
https://github.com/adrn/ipython/blob/master/examples/Notebook/Importing%20Notebooks.ipynb
Check out that notebook for full documentation and to understand the backgrounds. 

## Installation
`pip install nbimporter`

### Usage
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
