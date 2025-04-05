# plquery: query dataframes interactively

[![License][license-badge]](LICENSE)
[![Build Status][build-badge]][build]
[![Conda Platform][conda-badge]][conda-url]
[![Conda Downloads][conda-downloads-badge]][conda-url]
[![pypi-version][pypi-badge]][pypi]
[![python-version][python-version-badge]][pypi]

[license-badge]: https://img.shields.io/github/license/pavelzw/plquery?style=flat-square
[build-badge]: https://img.shields.io/github/actions/workflow/status/pavelzw/plquery/ci.yml?style=flat-square&branch=main
[build]: https://github.com/pavelzw/plquery/actions/
[conda-url]: https://prefix.dev/channels/conda-forge/packages/plquery
[conda-badge]: https://img.shields.io/conda/pn/conda-forge/plquery?style=flat-square&logoColor=white&logo=conda-forge
[conda-downloads-badge]: https://img.shields.io/conda/dn/conda-forge/plquery?style=flat-square
[pypi]: https://pypi.org/project/plquery
[pypi-badge]: https://img.shields.io/pypi/v/plquery.svg?style=flat-square&logo=pypi&logoColor=white
[python-version-badge]: https://img.shields.io/pypi/pyversions/plquery?style=flat-square&logoColor=white&logo=python

This tui allows you to query polars dataframes interactively by running polars expressions on parquet and CSV files from your system using [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop).

![plquery demo](.github/assets/demo/demo-light.gif#gh-light-mode-only)
![plquery demo](.github/assets/demo/demo-dark.gif#gh-dark-mode-only)

## 💿 Installation

You can install `plquery` from conda-forge or PyPi.
Once installed, you can run the `plquery` (or equivalently: `plq`) binary.

```bash
plquery my-df.parquet
# or
plq my-df.parquet
```

### conda-forge

```bash
pixi global install plquery
# or to run it in a temporary environment
pixi exec plquery my-df.parquet
# or
pixi exec plq my-df.parquet
```

### PyPi

```bash
pip install plquery
# or to run it in a temporary environment
uvx plquery my-df.parquet
```

## 📥 Development Setup

This project is managed by [pixi](https://pixi.sh).
You can install the package in development mode using:

```bash
git clone https://github.com/pavelzw/plquery
cd plquery

pixi run pre-commit-install
pixi run postinstall
pixi run test
```
