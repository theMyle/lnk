import win32com.client
from pathlib import Path
import typer


def create_shortcut(target_path: Path, shortcut_path: Path) -> bool:
    try:
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortcut(str(shortcut_path))
        shortcut.TargetPath = str(target_path)
        shortcut.Save()
        return True
    except Exception as e:
        typer.echo(f"Error creating shortcut: {e}", err=True)
        return False
