import importlib.metadata
import pathlib
import warnings

import polars as pl
from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Input, Markdown

try:
    __version__ = importlib.metadata.version(__name__)
except importlib.metadata.PackageNotFoundError as e:  # pragma: no cover
    warnings.warn(f"Could not determine version of {__name__}\n{e!s}", stacklevel=2)
    __version__ = "unknown"


def read_df(path: pathlib.Path) -> pl.DataFrame:
    if path.suffix == ".csv":
        df = pl.read_csv(path)
    elif path.suffix == ".parquet":
        df = pl.read_parquet(path)
    else:
        raise ValueError("Unsupported file format")
    return df


class PlqueryApp(App):
    def __init__(self, df: pl.DataFrame):
        self.df = df
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Input(placeholder='df.select(pl.col("..."))', id="input-query")
        with VerticalScroll(id="results-container"):
            yield Markdown(id="results")

    def on_input_submitted(self, message: Input.Submitted) -> None:
        try:
            df = self.df  # noqa: F841, used in `eval`
            res = eval(message.value)
            self.query_one("#results", Markdown).update(str(res))
        except Exception as e:
            self.query_one("#results", Markdown).update(str(e))
