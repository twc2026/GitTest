from rich.console import Console
from rich.panel import Panel

# 初始化 rich（第二个虚拟环境的第三方库）
console = Console()

class Directory:
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.files = []

class FileSystem:
    def __init__(self):
        self.root = Directory('/')

    def mkdir(self, path):
        parts = path.split('/')[1:]
        current = self.root
        for part in parts:
            if part not in current.children:
                current.children[part] = Directory(part)
            current = current.children[part]

    def touch(self, path):
        parts = path.split('/')
        file_name = parts[-1]
        dir_path = '/'.join(parts[:-1])
        current = self.root
        for part in dir_path.split('/')[1:]:
            if part in current.children:
                current = current.children[part]
            else:
                return
        current.files.append(file_name)

    def ls(self, path):
        parts = path.split('/')[1:]
        current = self.root
        for part in parts:
            if part in current.children:
                current = current.children[part]
            else:
                return []
        result = list(current.children.keys()) + current.files
        return ' '.join(sorted(result))


fs = FileSystem()

console.print(Panel("[bold green]✅ 虚拟文件系统已启动（运行在 venv2 环境，使用 rich 库）[/bold green]", width=60))

while True:
    try:
        line = console.input("[bold cyan]> ")
        if not line:
            continue
        operation, path = line.strip().split()

        if operation == 'mkdir':
            fs.mkdir(path)
            console.print(f"[bold blue]📁 已创建目录: {path}[/bold blue]")

        elif operation == 'touch':
            fs.touch(path)
            console.print(f"[bold magenta]📄 已创建文件: {path}[/bold magenta]")

        elif operation == 'ls':
            res = fs.ls(path)
            console.print(f"[bold yellow]{res}[/bold yellow]")

    except KeyboardInterrupt:
        console.print("\n[bold red]👋 程序退出[/bold red]")
        break
    except:
        console.print("[bold red]❌ 命令错误[/bold red]")