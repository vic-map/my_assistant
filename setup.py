from setuptools import setup

setup(
    name='assistant_project',
    description='CLI personal assistant',
    url='https://github.com/vic-map/assistant_project.git',
    author='project2 group',
    license='MIT',
    packag=['assistant_project'],
    install_requires=['markdown', 'datetime', 're',
                      'pathlib', 'os', 'json', 'pickle', 'shutil', 'sys'],
    entry_points={'console_scripts': [
        'my_assistant = assistant_project.assistant_f.py']}
)
