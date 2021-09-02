from setuptools import setup

setup(
    name='my_assistant',
    version='1.0',
    description='CLI personal assistant',
    url='https://github.com/vic-map/my_assistant/tree/main/my_assistant.git',
    author='project2 group',
    license='MIT',
    packag=['my_assistant'],
    install_requires=['markdown', 'datetime',
                      'pathlib', 'json', 'pickle', 'shutil', 'sys'],
    entry_points={'console_scripts': [
        'my_assistant = my_assistant.assistant_f']}
)
