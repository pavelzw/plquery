import pathlib
import sys

import polars as pl
from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Input, Markdown

pl.Config.set_tbl_formatting("MARKDOWN")


def read_df(path: pathlib.Path) -> pl.DataFrame:
    if path.suffix == ".csv":
        df = pl.read_csv(path)
    elif path.suffix == ".parquet":
        df = pl.read_parquet(path)
    else:
        raise ValueError("Unsupported file format")
    return df


class PlqApp(App):
    def compose(self) -> ComposeResult:
        yield Input(placeholder='df.select(pl.col("..."))', id="input-query")
        with VerticalScroll(id="results-container"):
            yield Markdown(id="results")

    def on_input_submitted(self, message: Input.Submitted) -> None:
        try:
            res = eval(message.value)
            self.query_one("#results", Markdown).update(str(res))
        except Exception as e:
            self.query_one("#results", Markdown).update(str(e))


def main():
    global df
    df = read_df(pathlib.Path(sys.argv[1]))
    app = PlqApp()
    app.run()


if __name__ == "__main__":
    main()
