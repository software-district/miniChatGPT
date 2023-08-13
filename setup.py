from setuptools import setup, find_packages

setup(
    name='minichatgpt',
    version='1.1.0',
    description='Mini Chatbot using GPT',
    author='eruigu',
    author_email='erick@ruigu.dev',
    packages=find_packages(),
    package_data={'minichatgpt':
                  ['model_training/intents.json', "frontend/**/*"]},
    install_requires=[
        'nltk~=3.8.1',
        'flask~=2.2.3',
        'numpy~=1.23.5',
        'python-dotenv~=1.0.0',
        'tensorflow~=2.12.0;platform_system=="Linux"',
        'tensorflow-macos~=2.12.0;platform_system=="Darwin"',
        'tensorflow-intel~=2.12.0;platform_system=="Windows"',
        'openai==0.27.0',
    ],
    entry_points={
        'console_scripts': [
            'minichatgpt = minichatgpt.backend.server:main',
        ],
    },
)
