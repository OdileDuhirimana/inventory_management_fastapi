import os

# Define the project structure as a dictionary
project_structure = {
    "fastapi_inventory": {
        "app": {
            "orders": ["models.py", "schemas.py", "crud.py", "routers.py"],
            "products": ["models.py", "schemas.py", "crud.py", "routers.py"],
            "users": ["models.py", "schemas.py", "crud.py", "routers.py"],
            "database.py": None,
            "dependencies.py": None,
            "main.py": None,
        },
        "requirements.txt": []
    }
}

def create_structure(base_path, structure):
    for folder, content in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)

        if isinstance(content, list):  # If the content is a list of files
            for file in content:
                open(os.path.join(folder_path, file), 'w').close()  # Create an empty file
        elif isinstance(content, dict):  # If the content is a dictionary (sub-folder)
            create_structure(folder_path, content)

# Starting path (You can change it if necessary)
base_path = "fastapi_inventory"

# Create the project structure
create_structure(base_path, project_structure)

print("Project structure created successfully.")
