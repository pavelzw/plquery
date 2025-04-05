# plquery: query dataframes interactively

[![CI](https://img.shields.io/github/actions/workflow/status/pavelzw/plquery/ci.yml?style=flat-square&branch=main)](https://github.com/pavelzw/plq/actions/workflows/ci.yml)
[![conda-forge](https://img.shields.io/conda/vn/conda-forge/plquery?logoColor=white&logo=conda-forge&style=flat-square)](https://prefix.dev/channels/conda-forge/packages/plq)
[![pypi-version](https://img.shields.io/pypi/v/plquery.svg?logo=pypi&logoColor=white&style=flat-square)](https://pypi.org/project/plq)
[![python-version](https://img.shields.io/pypi/pyversions/plquery?logoColor=white&logo=python&style=flat-square)](https://pypi.org/project/plq)

This tui allows you to query polars dataframes interactively by running polars expressions on parquet and CSV files from your system.

## 💿 Installation

### conda-forge

```bash
pixi global install plquery
# or to run it in a temporary environment
pixi exec plquery my-df.parquet
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
