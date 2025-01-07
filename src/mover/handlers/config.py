import os
from dotenv import load_dotenv


project_folder = "project_mover"
env_file_path = os.path.join(project_folder, ".env")

# Check if the project folder exists
if not os.path.exists(project_folder):
    print(f"Warning: Project folder '{project_folder}' not found.")
    print("Please run the init command to create the project folder and .env file")
    exit(1)

# Check if .env file exists
if not os.path.exists(env_file_path):
    print(f"Warning: .env file not found in {env_file_path}")
    print("Please run the init command to create the project folder and .env file")
    exit(1)

# Load the .env file
load_dotenv(env_file_path)

source = {}

source_db_host = os.getenv("SOURCE_DB_HOST", None)
source["host"] = source_db_host

source_db_port = os.getenv("SOURCE_DB_PORT", None)
source["port"] = source_db_port

source_db_user = os.getenv("SOURCE_DB_USER", None)
source["user"] = source_db_user

source_db_password = os.getenv("SOURCE_DB_PASSWORD", None)
source["password"] = source_db_password

source_db_name = os.getenv("SOURCE_DB_NAME", None)
source["database"] = source_db_name

destination = {}

destination_db_host = os.getenv("DESTINATION_DB_HOST", None)
destination["host"] = destination_db_host

destination_db_port = os.getenv("DESTINATION_DB_PORT", None)
destination["port"] = destination_db_port

destination_db_user = os.getenv("DESTINATION_DB_USER", None)
destination["user"] = destination_db_user

destination_db_password = os.getenv("DESTINATION_DB_PASSWORD", None)
destination["password"] = destination_db_password

destination_db_name = os.getenv("DESTINATION_DB_NAME", None)
destination["database"] = destination_db_name

def config_check_extended():
    """
    Load environment configuration from .env file in the project_mover directory.

    Attempts to find and load the .env file, printing out the loaded configuration.
    If the file or directory is not found, prints an informative message.
    """
    # Define the expected project folder and .env file path
    project_folder = "project_mover"
    env_file_path = os.path.join(project_folder, ".env")

    # Check if the project folder exists
    if not os.path.exists(project_folder):
        print(f"Warning: Project folder '{project_folder}' not found.")
        return

    # Check if .env file exists
    if not os.path.exists(env_file_path):
        print(f"Warning: .env file not found in {env_file_path}")
        return

    # Load the .env file
    load_dotenv(env_file_path)

    source_db_host = os.getenv("SOURCE_DB_HOST", None)
    print(source_db_host)
    source_db_port = os.getenv("SOURCE_DB_PORT", None)
    print(source_db_port)
    source_db_user = os.getenv("SOURCE_DB_USER", None)
    print(source_db_user)
    source_db_password = os.getenv("SOURCE_DB_PASSWORD", None)
    print(source_db_password)
    source_db_name = os.getenv("SOURCE_DB_NAME", None)
    print(source_db_name)

    destination_db_host = os.getenv("DESTINATION_DB_HOST", None)
    print(destination_db_host)
    destination_db_port = os.getenv("DESTINATION_DB_PORT", None)
    print(destination_db_port)
    destination_db_user = os.getenv("DESTINATION_DB_USER", None)
    print(destination_db_user)
    destination_db_password = os.getenv("DESTINATION_DB_PASSWORD", None)
    print(destination_db_password)
    destination_db_name = os.getenv("DESTINATION_DB_NAME", None)
    print(destination_db_name)
    # Print out the loaded environment variables
    print("Loaded Environment Configuration:")

    print("Source Database Configuration:")


def config_check():
    if source_db_host is None:
        print("Source Database Host: Not set")
    else:
        print("Source Database Host: Set")

    if source_db_port is None:
        print("Source Database Port: Not set")
    else:
        print("Source Database Port: Set")

    if source_db_user is None:
        print("Source Database User: Not set")
    else:
        print("Source Database User: Set")

    if source_db_password is None:
        print("Source Database Password: Not set")
    else:
        print("Source Database Password: Set")

    if source_db_name is None:
        print("Source Database Name: Not set")
    else:
        print("Source Database Name: Set")

    print("\nDestination Database Configuration:")
    if destination_db_host is None:
        print("Destination Database Host: Not set")
    else:
        print("Destination Database Host: Set")

    if destination_db_port is None:
        print("Destination Database Port: Not set")
    else:
        print("Destination Database Port: Set")

    if destination_db_user is None:
        print("Destination Database User: Not set")
    else:
        print("Destination Database User: Set")

    if destination_db_password is None:
        print("Destination Database Password: Not set")
    else:
        print("Destination Database Password: Set")

    if destination_db_name is None:
        print("Destination Database Name: Not set")
    else:
        print("Destination Database Name: Set")


if __name__ == "__main__":
    load_environment_config()
