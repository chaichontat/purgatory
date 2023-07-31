import json
from typing import Any

from rich.console import Console
from rich.syntax import Syntax


def jprint(d: Any, **kwargs: Any) -> None:
    console = Console()
    console.print(Syntax(json.dumps(d, indent=2), "json", **kwargs))
