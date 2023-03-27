import re

from setuptools import setup

requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

version = ""
with open("hoppercord/__init__.py") as f:
    match = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE)
    if match is None or match.group(1) is None:
        raise RuntimeError("version is not set")

    version = match.group(1)

if not version:
    raise RuntimeError("version is not set")

if any(v in version for v in ("a", "b", "rc")):
    # append version identifier based on commit count
    try:
        import subprocess

        p = subprocess.Popen(
            ["git", "rev-list", "--count", "HEAD"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = p.communicate()
        if out:
            version += out.decode("utf-8").strip()
        p = subprocess.Popen(
            ["git", "rev-parse", "--short", "HEAD"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = p.communicate()
        if out:
            version += "+g" + out.decode("utf-8").strip()
    except Exception:
        pass

readme = ""
with open("README.MD") as f:
    readme = f.read()

extras_require = {
    "voice": ["PyNaCl>=1.3.0,<1.5"],
    "docs": [
        "sphinx==5.2.3",
        "sphinxcontrib_trio==1.1.2",
        "sphinxcontrib-websupport",
        "typing_extensions>=4.2.0, <5",
    ],
    "speed": ["orjson>=3.5.4", "aiohttp[speedups]"],
}

packages = [
    "hoppercord",
    "hoppercord.types",
    "hoppercord.ui",
    "hoppercord.webhook",
    "hoppercord.ext.application_checks",
    "hoppercord.ext.commands",
    "hoppercord.ext.tasks",
    "hoppercord.ui.select",
    # Compat
    "discord",
    "discord.types",
    "discord.ui",
    "discord.webhook",
    "discord.ext.commands",
    "discord.ext.tasks",
]

setup(
    name="hoppercord",
    author="Border666",
    url="https://github.com/nextcord/nextcord",
    project_urls={
        "Issue tracker": "https://github.com/nextcord/nextcord/issues",
    },
    version=version,
    packages=packages,
    license="MIT",
    description="A Python wrapper for the Discord API forked from discord.py",
    long_description=readme,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    python_requires=">=3.8.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Framework :: AsyncIO",
        "Framework :: aiohttp",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)