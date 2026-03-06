from setuptools import setup, find_packages

setup(
    name="agencia-ia-automatizaciones",
    version="0.1.0",
    description="Plataforma de agentes IA con GitHub Actions integrados",
    author="devmv1979-star",
    author_email="dev.mv1979@gmail.com",
    url="https://github.com/devmv1979-star/agencia-ia-automatizaciones",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "python-dotenv==1.0.0",
        "requests==2.31.0",
        "openai==1.3.0",
        "pydantic==2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest==7.4.0",
            "pytest-cov==4.1.0",
            "black==23.9.1",
            "flake8==6.0.0",
            "isort==5.12.0",
            "bandit==1.7.5",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
)