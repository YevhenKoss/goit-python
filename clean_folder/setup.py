from setuptools import setup, find_namespace_packages

setup(
    name='clean',
    version='1.0.0',
    description='The script sorts files into folders',
    url='https://github.com/YevhenKoss/goit-python/tree/main/clean_folder',
    author='Yevhen Kosariev',
    author_email='kossik89@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean = clean_folder.clean:main']}
)