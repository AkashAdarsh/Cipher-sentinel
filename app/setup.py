from setuptools import setup, find_packages

setup(
    name="cipher-sentinel",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'uvicorn',
        'web3',
        'pydantic',
        'python-dotenv'
    ],
)