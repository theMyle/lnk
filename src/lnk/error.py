import typer

INVALID_SRC_MSG = (
    typer.style("[ERROR]: ", fg=typer.colors.RED)
    + typer.style("source ", fg=typer.colors.YELLOW)
    + "target is invalid/does not exist."
)

INVALID_DIR_MSG = (
    typer.style("[ERROR]: ", fg=typer.colors.RED)
    + "target destination directory does not exist."
)
