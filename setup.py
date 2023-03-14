from setuptools import setup, find_packages

install_requires = [
    "numpy>=1.19",  # 1.19 required by tensorflow 2.6
    "pandas>1.0.3,<2",
    "ipykernel>=4.6.1,<7",
    "jupyter>=1,<2",
    "black>=18.6b4,<21",
    "pytest>=3.6.4",
]

setup(
    name="Projectlib",
    version=1.0,
    install_requires=install_requires,
    package_dir={"Projectlib": "Projectlib"},
    python_requires=">=3.6, <3.10",
    packages=find_packages(where=".", exclude=["docs", "examples", "tests"]),
)
