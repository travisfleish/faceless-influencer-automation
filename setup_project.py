import os

# List of directories and their respective files
project_structure = {
    "app": [
        "__init__.py", "routes.py", "auth.py", "meme_scraper.py", "meme_generator.py",
        "scheduler.py", "instagram_api.py", "database.py", "config.py"
    ],
    "tests": [
        "test_routes.py", "test_auth.py", "test_scraping.py", "test_meme_generator.py", "test_instagram_api.py"
    ],
    "docs": [
        "setup_guide.md", "usage_guide.md", "api_documentation.md"
    ]
}

# List of files to create directly in the root directory
root_files = [".gitignore", ".env", "README.md"]

# Function to create directories
def create_directories(base_dir, structure):
    for directory in structure:
        dir_path = os.path.join(base_dir, directory)
        os.makedirs(dir_path, exist_ok=True)  # Create directory if it doesn't exist

# Function to create files in the root or specified directories
def create_files(base_dir, structure):
    for directory, files in structure.items():
        for file in files:
            file_path = os.path.join(base_dir, directory, file)
            if not os.path.exists(file_path):  # Create file only if it doesn't already exist
                with open(file_path, 'w') as f:
                    pass  # Create an empty file

# Create the root files
for file in root_files:
    file_path = os.path.join(".", file)
    if not os.path.exists(file_path):  # Create file only if it doesn't already exist
        with open(file_path, 'w') as f:
            pass  # Create an empty file

# Create directories and their respective files
create_directories(".", project_structure)
create_files(".", project_structure)

print("Project structure created successfully!")
