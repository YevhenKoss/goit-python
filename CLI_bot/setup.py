from setuptools import setup, find_namespace_packages

setup(
    name='CLIBot',
    version='1.0.0',
    description='With the help of this script, an assistant is implemented which creates a phone book and edits it',
    url='https://github.com/YevhenKoss/goit-python/tree/main/CLI_bot',
    author='Yevhen Kosariev',
    author_email='kossik89@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['bot = CLIBot.main:main']}
)