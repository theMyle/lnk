import typer
import pathlib
from typing import Optional
from . import shortcut


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

    if output is not None:
        out_name = pathlib.Path(output).stem + ".lnk"
    else:
        out_name = src.stem + ".lnk"

    shortcut_path = dest.joinpath(out_name)

    success = shortcut.create_shortcut(src, shortcut_path)
    if not success:
        typer.echo(
            typer.style("[ERROR]: ", fg=typer.colors.RED)
            + "Failed to create shortcut.",
            err=True,
        )
        raise typer.Exit(1)

    typer.echo(
        typer.style("[SUCCESS]: ", fg=typer.colors.GREEN)
        + f"Shortcut created at {shortcut_path}"
    )


if __name__ == "__main__":
    app()
