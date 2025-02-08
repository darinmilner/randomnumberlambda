Explanation of pyproject.toml:
Project Metadata:

name: The name of your project.

version: The version of your project.

description: A short description of your project.

authors: Your name and email.

Dependencies:

python: Specifies the Python version (3.9 in this case).

pytest and pytest-cov: Added as development dependencies under [tool.poetry.dev-dependencies].

Build System:

Specifies that Poetry is used to build the project.

Install Poetry Locally
If you don’t have Poetry installed, you can install it by following the official instructions: https://python-poetry.org/docs/#installation.

Once Poetry is installed, run the following command in your project directory to set up the virtual environment and install dependencies:

poetry install