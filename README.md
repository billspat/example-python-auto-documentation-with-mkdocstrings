
# Auto-Generated Python Project Documentation with MkDocs

This repo is my investigation of automatic python project documentation using [mkdocs](https://github.com/mkdocs/mkdocs), [mkdocstrings](https://github.com/mkdocstrings/mkdocstrings) and [Material for MkDocs](https://github.com/squidfunk/mkdocs-material). The code is then hosted on GitHub pages, with automatic deployment using [GitHub Actions](https://docs.github.com/en/actions). 

At the moment, most of the code in this repo is copied and pasted from the Real Python tutorial [Build Your Python Project Documentation With MkDocs](https://realpython.com/python-project-documentation-with-mkdocs/). 

You can browse the static build of the documentation here: https://J-sephB-lt-n.github.io/python-auto-documentation-with-mkdocstrings/dfsdf

# Instructions/Explanation of the Documentation Process 

* Refer to [requirements.txt](./requirements.txt) for the required packages (excluding mypy).

* The initial MkDocs files were created by running <code>mkdocs new .</code> in terminal from the root project directory. This creates the files [makedocs.yml](./makedocs.yml) and [/docs/index.md](./docs/index.md).

* [makedocs.yml](./makedocs.yml) contains settings controlling the documentation style and behaviour.

* This code in [makedocs.yml](./makedocs.yml) enables the documentation to automatically extract information from the docstrings in the code itself: 

```yaml
plugins:
  - mkdocstrings
```

* The documentation can be hosted locally by running <code>mkdocs serve</code> in terminal from the root project directory (view the documentation in the browser by going to the localhost URL specified - it will be something like http://localhost:8000).

