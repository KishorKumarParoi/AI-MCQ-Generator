from setuptools import setup, find_packages

setup(
    name='mcqgenerator',
    version='0.1',
    author='Kishor Paroi',
    author_email='Kishor.ruet.cse@gmail.com',
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages(),
)