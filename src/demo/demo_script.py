from rich.console import Console
from rich.table import Table
import requests

console = Console()

def show_health(api="http://localhost:8000"):
    r = requests.get(f"{api}/health", timeout=5)
    console.rule("[bold green]Health")
    console.print(r.json())

def show_topics(api="http://localhost:8000", limit=5):
    r = requests.get(f"{api}/topics", params={"limit": limit}, timeout=10)
    items = r.json().get("items", [])
    table = Table(title="Top Topics")
    table.add_column("Name")
    table.add_column("Count")
    for it in items:
        table.add_row(str(it.get("name")), str(it.get("count")))
    console.print(table)

def main():
    show_health()
    show_topics()

if __name__ == "__main__":
    main()
