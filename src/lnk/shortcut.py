import win32com.client
from pathlib import Path
import typer


def create_shortcut(
    target_path: Path,
    output_path: Path,
    arguments: str | None = None,
    working_dir: Path | None = None,
) -> bool:
    try:
        shell = win32com.client.Dispatch("WScript.Shell")

        shortcut = shell.CreateShortcut(str(output_path))
        shortcut.TargetPath = str(target_path)

        if working_dir:
            shortcut.WorkingDirectory = str(working_dir)

        if arguments:
            shortcut.Arguments = arguments

        shortcut.Save()
        return True
    except Exception as e:
        typer.echo(f"Error creating shortcut: {e}", err=True)
        return False
