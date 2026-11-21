from rich import print
from rich.table import Table

print("[bold green]rich 装好了！[/bold green]")
print("[red]红色[/red] [blue]蓝色[/blue] [yellow]黄色[/yellow]")

table = Table(title="我的待办清单")
table.add_column("编号", style="cyan")
table.add_column("任务", style="white")
table.add_row("1", "学 pip")
table.add_row("2", "学虚拟环境")

print(table)