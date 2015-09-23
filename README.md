# nbimporter
Import ipython notebooks as modules

## Origin
The code is taken entirely from https://github.com/adrn/ipython/blob/master/examples/Notebook/Importing%20Notebooks.ipynb. 
Check out that notebook for full documentation and to understand the backgrounds. 

## Installation
`pip install nbimporter`

### Usage
**Notebook foo.ipynb:**

In[1]:
```python
def a(): 
    print("Hello World"!)
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
