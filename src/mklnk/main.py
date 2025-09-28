import typer
import pathlib
from typing import Optional

app = typer.Typer()


@app.command(no_args_is_help=True)
def mklnk(
    source: str = typer.Argument(
        ...,
        help="Source file or source directory.",
    ),
    destination: str = typer.Argument(
        ...,
        help="Target destination path.",
    ),
    output: Optional[str] = typer.Option(
        None,
        help="Set output file name.",
    ),
):
    """

    Create a shortcut/lnk file to the target destination directory.

    """

    INVALID_SRC_MSG = (
        typer.style("[ERROR]: ", fg=typer.colors.RED)
        + typer.style("source ", fg=typer.colors.YELLOW)
        + "target is invalid/does not exist."
    )

    INVALID_DEST_MSG = (
        typer.style("[ERROR]: ", fg=typer.colors.RED)
        + "target destination directory does not exist."
    )

    # check if source exists/valid
    # check if destination is valid
    # check if user supplied output name else use default/inferred

    src = pathlib.Path(source).resolve()
    if not src.exists():
        typer.echo(INVALID_SRC_MSG, err=True)
        raise typer.Exit(1)

    dest = pathlib.Path(destination).resolve()
    if not dest.is_dir():
        typer.echo(INVALID_DEST_MSG, err=True)
        raise typer.Exit(1)

    out = src.stem + ".lnk"
    if output is not None:
        out = pathlib.Path(output)
        out = out.stem + ".lnk"

    print(f"source: {src}")
    print(f"dest: {dest}")
    print(f"output: {dest.joinpath(out)}")


def main():
    app()


if __name__ == "__main__":
    main()
