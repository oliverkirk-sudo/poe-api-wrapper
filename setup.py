# coding: utf-8
from setuptools import setup, find_packages
from pathlib import Path

base_path = Path(__file__).parent
long_description = (base_path / "README.md").read_text(encoding='utf-8')

VERSION = '1.2.7'
DESCRIPTION = 'A simple API wrapper for Poe.com using Httpx'
LONG_DESCRIPTION = '👾 A Python API wrapper for Poe.com, using Httpx. With this, you will have free access to ChatGPT, Claude, Llama, Google-PaLM and more! 🚀'

setup(
    name="poe-api-wrapper",
    version=VERSION,
    author="snowby666",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=['httpx', 'websocket-client', 'requests_toolbelt', 'loguru'],
    extras_require={
        'proxy': ['ballyregan; python_version>="3.9"']
    },
    keywords=['python', 'poe', 'quora', 'chatgpt', 'claude', 'poe-api', 'api'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent"
    ],
    url="https://github.com/snowby666/poe-api-wrapper"
)
# ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
# yiri-mirai 0.2.6.1 requires aiofiles<0.8.0,>=0.7.0, but you have aiofiles 23.2.1 which is incompatible.
# yiri-mirai 0.2.6.1 requires httpx<0.19.0,>=0.18.2, but you have httpx 0.25.0 which is incompatible.
# yiri-mirai 0.2.6.1 requires websockets<10.0,>=9.1, but you have websockets 11.0.3 which is incompatible.
