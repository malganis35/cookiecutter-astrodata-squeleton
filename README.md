# Cookiecutter AstroData Squeleton

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._

This project is based on Cookiecutter Data Science : [Project homepage](http://drivendata.github.io/cookiecutter-data-science/)

## Requirements to use the cookiecutter template:
- uv

## To start a new Data Science project, run:

``` bash
uv run --with cookiecutter cookiecutter git@github.com:malganis35/cookiecutter-astrodata-squeleton.git --directory="data-science"
```

Alternatively, you can add an alias to call this template in UNIX:

``` bash
alias ds-make='uv run --with cookiecutter cookiecutter git@github.com:malganis35/cookiecutter-astrodata-squeleton.git --directory="data-science"'
```

## To start a new Sphinx documentation project, run:


``` bash
uv run --with cookiecutter cookiecutter git@github.com:malganis35/cookiecutter-astrodata-squeleton.git --directory="sphinx-docs"
```

Alternatively, you can add an alias to call this template in UNIX:

``` bash
alias docs-make='uv run --with cookiecutter cookiecutter git@github.com:malganis35/cookiecutter-astrodata-squeleton.git --directory="sphinx-docs"'
```

