from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    version='0.9.4+sbo.4',
    name='FuelSDK-sbo',
    description='ExactTarget Fuel SDK for Python',
    long_description=readme,
    author='ExactTarget',
    author_email='code@exacttarget.com',
    py_modules=['ET_Client'],
    packages=['FuelSDK'],
    url='https://github.com/ExactTarget/FuelSDK-Python',
    license='MIT',
    install_requires=[
        'pyjwt>=0.3.2',
        'requests>=2.5.1',
        'suds-jurko==0.6',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3.7',
    ],
)
