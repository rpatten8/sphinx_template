# Sphinx Auto Docs Template
A template project to be used for doc generation without cluttering source project with unnecessary packages.

## How to use

- Make a new local branch
- Delete app.py and conf.py
- Copy files from source project to:

```sphinx_template > project_folder```

- Open the index.rst file within docs
- for each new py file add:


![img_2.png](img_2.png)
  
  
- In terminal (if not already there):

```
cd docs

make latex
```

- Open TeXworks 
- Navigate to docs folder, latex then open the .tex file
- Run