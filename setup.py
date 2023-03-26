import setuptools

with open('readme.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='clacks_qt',
    version='0.0.1',
    author='Mattias Van Camp',
    author_email='mavcart.mvc@gmail.com',
    description='Extension library for the clacks framework to allow it to work within Qt-compatible applications.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MaVCArt/clacks_qt',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
