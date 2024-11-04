#  

---
## Authors
* [list of all contributors, with their institutional email and ORCID]


## License
CC-BY-SA 4.0, see attached License.md

---
## Description

This repo contains a module which puts together a set of useful functions which we (the TOME project) use for preprocessing latin texts.


## Getting started

1. go to terminal and clone the repository:
```bash
git clone https://github.com/CCS-ZCU/latin-preprocessing.git
```
2. open a python script where you want to use the module (it can be located anywhere on your machine)
3. check that you use an appropriate python interpreter (virtual environment or kernel, in case of jupyter (e.g. `latin_global_kernel`, if you are on CCS-Lab's jupyterhub server...)
4. specify relative or absolute path to the module subfolder within your local clone of the repository (
For instance:
```python
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../latin-preprocessing'))`)
```
4. Add the directory to sys.path if it's not already there
```python
if module_path not in sys.path:
    sys.path.insert(0, module_path)
```
5. Import the module
```python
import tomela
```

6. If you later make changes to the tomela module and want to reload it:
```
importlib.reload(tomela)
```

## How to cite

[once a release is created and published via zenodo, put its citation here]

## Ackwnowledgement

[This work has been supported by ...]
