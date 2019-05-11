import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="my_pack",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    url="https://github.com/graciofilipe/pack",
    packages=setuptools.find_packages(),
    install_requires=['numpy'],
    entry_points={'console_scripts':
                      ['add_two=my_pack.main_run:main']}
)