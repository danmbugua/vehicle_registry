from setuptools import setup


setup(
    name="vehicles",
    version="0.1.0a1",
    packages=[
        'vehicles',
        'vehicles.migrations',
    ],

    description="Vehicles registry sample project",
    long_description=open('README.rst').read(),
    url="",
    author="marika",
    author_email="marika@savannahinformatics.com",
    license="Proprietary",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        "Django==1.8",
        "django-filter==0.10.0",
        "djangorestframework==3.1.2",
        "pytest==2.7.0",
        "pytest-django==2.8.0"
    ],
)
