import secrets
import string
import hashlib
import socket
from rich.console import Console
from rich.panel import Panel

console = Console()

# ====================== PASSWORD GENERATOR ======================
def generate_password(length=16):
    if length < 8:
        length = 8
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


# ====================== PASSWORD STRENGTH CHECKER ======================
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 3
    elif len(password) >= 8:
        score += 2
    else:
        feedback.append("Password is too short")

    if any(c.isupper() for c in password): score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in "!@#$%^&*" for c in password): score += 2

    # Common passwords
    common = ["password", "123456", "qwerty", "admin", "letmein", "welcome"]
    if password.lower() in common:
        score = 0
        feedback.append("Very common password - change it!")

    if score >= 7:
        crack_time = "Hundreds of years"
    elif score >= 5:
        crack_time = "Months to years"
    elif score >= 3:
        crack_time = "Days to weeks"
    else:
        crack_time = "Less than a day"

    return score, feedback, crack_time


# ====================== HASH GENERATOR ======================
def generate_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()


# ====================== PORT SCANNER ======================
def port_scanner(target="127.0.0.1", max_ports=200):
    console.print(f"[yellow]Scanning {target} (up to port {max_ports})...[/yellow]")
    console.print("[dim]This may take a few seconds...[/dim]")
    
    open_ports = []
    for port in range(1, max_ports + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.8)                    # Increased timeout
            result = s.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
                console.print(f"[green]✓ Port {port} is OPEN[/green]")
            s.close()
        except:
            pass
    
    if not open_ports:
        console.print("[yellow]No open ports found in the scanned range.[/yellow]")
        console.print("[dim]Sometimes firewalls and windows wont allow this to complete or a timeout occured[/dim]")
    else:
        console.print(f"\n[bold green]Found {len(open_ports)} open ports![/bold green]")
    
    return open_ports