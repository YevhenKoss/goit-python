from setuptools import setup, find_namespace_packages

setup(
    name='clean',
    version='1.0.0',
    description='The script sorts files into folders',
    url='http://github.com/dummy_user/useful',
    author='Flying Circus',
    author_email='flyingcircus@example.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts': ['helloworld = useful.some_code:hello_world']}
)