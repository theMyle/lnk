import typer
import pathlib
from typing import Optional
from . import shortcut, utils, error


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
        help="Sets a custom output name.",
    ),
    args: Optional[str] = typer.Option(
        None,
        help="Pass additional command-line arguments when the shortcut launches the target.",
    ),
    workDir: Optional[str] = typer.Option(
        None, help="Set the working directory used when launching from the shortcut."
    ),
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        callback=utils.version_callback,
        is_eager=True,
        is_flag=True,
        help="Show version and exit.",
    ),
):
    """

    Create a shortcut/lnk file to the target destination directory.

    """

    # check if source exists/valid
    src = pathlib.Path(source).resolve()
    if not src.exists():
        typer.echo(error.INVALID_SRC_MSG, err=True)
        raise typer.Exit(1)

    # check if destination is valid
    dest = pathlib.Path(destination).resolve()
    if not dest.is_dir():
        typer.echo(error.INVALID_DIR_MSG, err=True)
        raise typer.Exit(1)

    # check if user supplied output name else use default/inferred
    if output is not None:
        out_name = pathlib.Path(output).stem + ".lnk"
    else:
        out_name = src.stem + ".lnk"

    # check if supplied dir is valid
    wd = pathlib.Path(source).parent.resolve()
    if workDir:
        wd = pathlib.Path(workDir).absolute().resolve()
        if not wd.is_dir():
            typer.echo(error.INVALID_DIR_MSG, err=True)
            raise typer.Exit(1)

    shortcut_path = dest.joinpath(out_name)

    success = shortcut.create_shortcut(src, shortcut_path, args, wd)
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
