from setuptools import setup 

setup(
    name='vampfetch',  # The name of your package
    version='0.1.0',  # Version number
    description='A simple system info fetching tool',  # Short description
    long_description=open('README.md').read(),  # Detailed description from README
    long_description_content_type='text/markdown',  # The format of the long description
    author='Ansh Agarwal',  # Your name
    author_email='anshag2007@gmail.com',  # Your email
    url='https://github.com/anshag2007/vampfetch',  # URL of your project (optional)
    packages=['.'],  # List of packages to include (your project directory)
    install_requires=[
        'psutil',  # List any dependencies
        'py-cpuinfo'
    ],
    entry_points={
        'console_scripts': [
            'vampf = vampf:exc',  # Main function to be called when running `vampf`
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Linux',
    ],
    license='MIT',  # Choose your license
    python_requires='>=3.6',  # Python version requirement
)

