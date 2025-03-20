from setuptools import setup, find_packages

setup(
    name="cipher-sentinel",
    version="0.1.0",
    description="AI-powered smart contract auditor and rug pull analyzer",
    author="Akash Adarsh",
    author_email="akash2406@gmail.com",
    packages=find_packages(),
    install_requires=[
        'fastapi>=0.115.11',
        'uvicorn>=0.34.0',
        'pydantic>=2.10.6',
        'web3>=7.8.0',
        'slither-analyzer>=0.9.6',
        'celery>=5.3.6',
        'redis>=5.2.1',
        'python-dotenv>=1.0.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.1',
            'pytest-asyncio>=0.21.0',
            'black>=24.2.0',
            'isort>=5.13.2',
            'flake8>=7.0.0',
        ],
        'ml': [
            'torch>=2.0.0',
            'transformers>=4.30.0',
            'scikit-learn>=1.0.0',
            'numpy>=1.24.0',
            'pandas>=2.0.0',
        ],
    },
    python_requires='>=3.11',
) 