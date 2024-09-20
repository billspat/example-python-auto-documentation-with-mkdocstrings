
# Auto-Generated Python Project Documentation with MkDocs

This repo is my investigation of automatic python project documentation using [MkDocs](https://github.com/mkdocs/mkdocs), [MkDocStrings](https://github.com/mkdocstrings/mkdocstrings) and [Material for MkDocs](https://github.com/squidfunk/mkdocs-material). The documentation is then hosted on [GitHub pages](https://pages.github.com), with automatic deployment using [GitHub Actions](https://docs.github.com/en/actions). 

The structure of this repo is from the [Real Python](https://realpython.com) tutorial [Build Your Python Project Documentation With MkDocs](https://realpython.com/python-project-documentation-with-mkdocs/). 

You can browse the static build of the documentation here: https://J-sephB-lt-n.github.io/python-auto-documentation-with-mkdocstrings/

# Instructions/Explanation of the Documentation Process 

### *completely stolen (forked) from https://github.com/J-sephB-lt-n*

* Refer to [requirements.txt](./requirements.txt) for the required packages.  

* The initial MkDocs files were created by running <code>mkdocs new .</code> in terminal from the root project directory. This command creates the files [makedocs.yml](./makedocs.yml) and [/docs/index.md](./docs/index.md).

* [makedocs.yml](./makedocs.yml) contains settings controlling the documentation style and behaviour.

* This code in [makedocs.yml](./makedocs.yml) enables the documentation to automatically extract information from the docstrings in the code itself: 

```yaml
plugins:
  - mkdocstrings
```

* In order to specify which docstrings should be included in the documentation, add links into the markdown using the triple-colon format e.g. <code>::: link.to.python.module</code>

* The documentation is built by combining and rendering the markdown files in the [/docs/](./docs/) folder.

* The documentation can be hosted locally by running <code>mkdocs serve</code> in terminal from the root project directory (view the documentation in the browser by going to the localhost URL specified - it will be something like http://localhost:8000).

* The documentation can be rendered into static html using the terminal command <code>mkdocs build</code>. The output is written to the folder [/site/](./site/), which should be added to the [.gitignore](./.gitignore) file.

* If the project code is already inside a GitHub repository, the documentation can be hosted (for free) on GitHub pages (at the url https://your-user-name.github.io/your-repo-name/) by running the terminal command <code>mkdocs gh-deploy</code>.

# Automatic GitHub Deployment of Documentation

Adding the yaml file [.github/workflows/deploy_documentation.yml](./.github/workflows/deploy_documentation.yml) causes the documentation to be automatically deployed (i.e. runs the code <code>mkdocs gh-deploy</code>) whenever there is a push to the main branch of this repo.

Note also that for this process to work, you need to give GitHub actions "Read and Write permissions" on this repo. I did this using the GitHub website GUI - the setting is available under Settings->Actions->General.

# References 

* https://realpython.com/python-project-documentation-with-mkdocs/

* https://numpydoc.readthedocs.io/en/latest

* https://blog.elmah.io/deploying-a-mkdocs-documentation-site-with-github-actions/
