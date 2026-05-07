from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.panel import Panel
import tools

console = Console()

def main():
    console.print(Panel.fit(
        "[bold green]🔐 Zer0 CyberGuard Toolkit[/bold green]\n"
        "[cyan]Personal Cybersecurity Utilities[/cyan]\n"
        "[dim]By Jordan Martin[/dim]",
        border_style="green"
    ))

    while True:
        console.print("\n[bold]Available Tools:[/bold]")
        console.print("1. 🔑 Strong Password Generator")
        console.print("2. 🔍 Password Strength Checker")
        console.print("3. 🔐 Hash Generator (SHA-256)")
        console.print("4. 📡 Basic Port Scanner")
        console.print("5. Exit")

        choice = Prompt.ask("Select a tool", choices=["1", "2", "3", "4", "5"])

        if choice == "1":
            length = IntPrompt.ask("Password length", default=16)
            pwd = tools.generate_password(length)
            console.print(Panel(f"[bold green]{pwd}[/bold green]", title="Generated Password"))

        elif choice == "2":
            pwd = Prompt.ask("Enter password to check")
            score, feedback, crack_time = tools.check_password_strength(pwd)
            color = "green" if score >= 6 else "yellow" if score >= 4 else "red"
            console.print(Panel(f"Strength: [{color}]{score}/8[/] | Estimated crack time: [bold]{crack_time}[/]", title="Password Analysis"))
            if feedback:
                console.print("[red]Suggestions:[/red]")
                for item in feedback:
                    console.print(f"   • {item}")

        elif choice == "3":
            text = Prompt.ask("Enter text to hash")
            result = tools.generate_hash(text)
            console.print(Panel(result, title="SHA-256 Hash"))

        elif choice == "4":
            target = Prompt.ask("Enter target IP (default localhost)", default="127.0.0.1")
            max_p = IntPrompt.ask("How many ports to scan?", default=100)
            tools.port_scanner(target, max_p)

        elif choice == "5":
            console.print("[green]Thank you for using Zer0 CyberGuard Toolkit![/]")
            break

if __name__ == "__main__":
    main()