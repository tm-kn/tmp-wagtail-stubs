from setuptools import find_packages, setup

dependencies = ["mypy>=0.790", "django-stubs>=1.7.0", "typing-extensions>=3.7.2"]
setup(
    name="wagtail-stubs",
    version="0.1.0",
    install_requires=dependencies,
    packages=["wagtail-stubs"],
    package_data={"wagtail-stubs": ["*.pyi"]},
    python_requires=">=3.6",
)
