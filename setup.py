import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='(package name)', # insert the name of your package here
    version='(version)', # insert your version here using this format: 0.0.0. Packages will only be updated if this value is changed
    author='(name)', # insert your name here
    author_email='(email)', # insert your email here, this is so people can contact you
    description='(description)', # insert a description here
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='(link)', # insert the link to your GitHub repo here
    project_urls = {}, # insert necessary URLs here
    license='MIT', # license type
    packages=['rfunctions'], # the directory to your package
)