import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='teganmath', # insert the name of your package here
    version='0.0.0', # insert your version here using this format: 0.0.0. Packages will only be updated if this value is changed
    author='Tegan', # insert your name here
    author_email='', # insert your email here, this is so people can contact you
    description='This package allows you to add two numbers (teganmath)', # insert a description here
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="github.com/teganr/my-package", # insert the link to your GitHub repo here
    #project_urls = {}, # insert necessary URLs here
    license='MIT', # license type
    packages=['teganmath'], # the directory to your package
)
