from setuptools import find_packages, setup

def get_requirements(file_path: str):
    with open(file_path, 'r') as file_obj:
        requirements = [line.strip() for line in file_obj]

    return requirements

setup(
    name='mlproject1',
    version='0.0.1',
    author='mani',
    author_email='manianantharaj1990@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),  # Fixed the filename
)
