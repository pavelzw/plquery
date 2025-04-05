import pathlib
import sys

import polars as pl

from . import PlqueryApp, read_df


def main():
    pl.Config.set_tbl_formatting("MARKDOWN")
    df = read_df(pathlib.Path(sys.argv[1]))
    app = PlqueryApp(df)
    app.run()


if __name__ == "__main__":
    main()
