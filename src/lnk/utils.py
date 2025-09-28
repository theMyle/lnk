import typer


def version_callback(value: bool):
    if value:
        try:
            from importlib.metadata import version

            app_version = version("lnk")
        except ImportError:
            app_version = "0.1.0"
        typer.echo(f"lnk version {app_version}")
        raise typer.Exit()
