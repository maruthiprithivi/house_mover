import click

from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from rich import box
from time import sleep

from mover.handlers.config import config_check, config_check_extended


@click.group()
def main():
    """House Mover CLI"""
    pass


@main.command()
@click.option("--source", prompt="Source location", help="Source location of the house")
@click.option(
    "--destination",
    prompt="Destination location",
    help="Destination location of the house",
)
def move(source, destination):
    """Move a house from source to destination."""
    click.echo(f"Moving house from {source} to {destination}!")


@main.command()
def list():
    """List all houses."""
    click.echo("Listing all houses!")


@main.command()
@click.confirmation_option(
    prompt="We are about to initialize a house mover project. Do you want to proceed?"
)
def init():
    """Initialize the project by creating a project_mover folder with a .env file from the template."""
    import shutil
    import os

    template_path = "mover/templates/.env_template"
    project_folder = "project_mover"
    env_path = os.path.join(project_folder, ".env")

    # Create project folder if it doesn't exist
    os.makedirs(project_folder, exist_ok=True)

    # Check if .env file already exists
    if not os.path.exists(env_path):
        shutil.copy(template_path, env_path)
        click.echo(
            f"Initialized project in {project_folder} with environment file: {env_path}"
        )
    else:
        click.echo(
            f"Project folder {project_folder} already exists with an environment file"
        )


@main.command()
@click.option(
    "--check",
    "-C",
    is_flag=True,
    help="Check the current configuration without loading.",
)
def config(check):
    """Configure the project by setting the environment variables."""

    if check:
        click.echo("Checking current configuration...")
        # Here you can add logic to display current configuration without loading
        # For example, you might want to read from the .env file and print the values
    else:
        x = ""
        print("This is the config", x)

"""
Reference for interactive cli utility
"""
# console = Console()

# @click.group(invoke_without_command=True)
# def main():
#     """House Mover CLI"""
#     console.rule("[bold blue]Welcome to the House Mover CLI[/bold blue]")
#     while True:
#         display_menu()
#         choice = click.prompt("[bold green]Enter your choice[/bold green]", type=int)

#         if choice == 1:
#             move_house()
#         elif choice == 2:
#             check_status()
#         elif choice == 3:
#             console.rule("[bold red]Exiting the utility. Goodbye![/bold red]")
#             break
#         else:
#             console.print("[bold red]Invalid choice. Please try again.[/bold red]")

# def display_menu():
#     """Displays the main menu with Rich styling."""
#     console.print("\n[bold magenta]Choose an action:[/bold magenta]")
#     table = Table(show_header=False, box=box.SIMPLE)
#     table.add_row("[bold cyan]1[/bold cyan]", "Move a house")
#     table.add_row("[bold cyan]2[/bold cyan]", "Check status")
#     table.add_row("[bold cyan]3[/bold cyan]", "Exit")
#     console.print(table)

# def move_house():
#     """Interactive function to move a house."""
#     # source = click.prompt("[bold yellow]Enter the source location[/bold yellow]")
#     # console.print("[bold yellow]Enter the source location :[/bold yellow]", end="")
#     # source = click.prompt("", type=str, default="", show_default=False, show_choices=False)
#     source = click.prompt(click.style("Enter the source location", fg='yellow'), type=str, default="", show_default=False, show_choices=False)
#     destination = click.prompt("[bold yellow]Enter the destination location[/bold yellow]")

#     console.print(f"[bold green]Moving house from {source} to {destination}...[/bold green]")

#     # Simulate a loading animation with progress bar
#     with Progress() as progress:
#         task = progress.add_task("[cyan]Processing move...[/cyan]", total=100)
#         for _ in range(20):
#             sleep(0.1)
#             progress.update(task, advance=5)

#     console.print("[bold green]House move completed successfully![/bold green]")

# def check_status():
#     """Interactive function to check the status."""
#     console.print("[bold yellow]Checking system status...[/bold yellow]")

#     # Simulate a loading animation
#     with Progress() as progress:
#         task = progress.add_task("[cyan]Fetching status...[/cyan]", total=100)
#         for _ in range(20):
#             sleep(0.1)
#             progress.update(task, advance=5)

#     console.print("[bold green]All systems are operational![/bold green]")

if __name__ == "__main__":
    main()
