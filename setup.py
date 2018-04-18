from setuptools import setup, find_packages


setup(name="django-smart-selects",
      version="1.0.4",
      description="Django application to handle chained model fields.",
      long_description=long_desc,
      author="Patrick Lauber",
      author_email="digi@treepy.com",
      url="https://github.com/digi604/django-smart-selects",
      packages=find_packages(),
      include_package_data=True,
      tests_require=[
          'flake8',
      ],
      )