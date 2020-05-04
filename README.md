## techtalentsouth

Tech Talent South Enablement

## Documentation

Tech Talent South [Data Science Setup and Installation Checklist](http://qlx.services/enablement/files/TTSDataScienceChecklist.pdf) (QLX). Copyright 2020 Qualex Consulting Services Incorporated.

[A Whirlwind Tour of Python by Jake VanderPlas](http://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf) (O’Reilly). Copyright 2016 O’Reilly Media, Inc., 978-1-491-96465-1.

[Python Data Science Handbook by Jake VanderPlas](https://github.com/jakevdp/PythonDataScienceHandbook) (O’Reilly). Copyright 2016 O’Reilly Media, Inc., 978-1-491-91205-8.

- - -

## Useful Links

**Github** - https://github.com/enterlifeonline/techtalentsouth

**Viewer** - https://nbviewer.jupyter.org/github/enterlifeonline/techtalentsouth/tree/master/

**Slack** - https://tts-students.slack.com

**Tools** 

- Powershell - https://aka.ms/powershell
- Hyper - https://hyper.is 
- Git Bash (for Windows) - https://gitforwindows.org/

- - -

## Software

Anaconda is a free and open-source[6] distribution of the Python and R programming languages for scientific computing (data science, machine learning applications, large-scale data processing, predictive analytics, etc.), that aims to simplify package management and deployment. The distribution includes data-science packages suitable for Windows, Linux, and macOS. 

- Anaconda (packages included) - https://www.anaconda.com/products/individual
- Miniconda (only Conda and Python packages included) - https://docs.conda.io/en/latest/miniconda.html

### Installation

To install the requirements using [conda](http://conda.pydata.org), run the following at the command-line:

```
$ conda install --file requirements.txt
```

To create a stand-alone environment named ``PDSH`` with Python 3.5 and all the required package versions, run the following:

```
$ conda create -n PDSH python=3.5 --file requirements.txt
```

You can read more about using conda environments in the [Managing Environments](http://conda.pydata.org/docs/using/envs.html) section of the conda documentation.

### Markup Language

- [Markup Language Cheatsheet](http://qlx.services/enablement/files/readmeMD.pdf)

## Code Editors

- Microsoft Visual Studio - https://visualstudio.microsoft.com/downloads/
- Sublime 3 - https://www.sublimetext.com/3
- Atom - https://atom.io/

## Cloud
- [Microsoft Azure](https://azure.microsoft.com/)

- - - 

## Package Application Managers

You can install the executables of Anaconda, Conda, Python or you can use a Package Application Manager that is applicable to your operating system. This allows you to maintain, update, install and configure all the necessary software components via automated scripting.

- [Brew (OS X, Linux)](https://brew.sh/)
- [Chocolatey (Windows)](https://chocolatey.org/)

## What is BREW?

For Mac OS, Linux

Home-brew installs the stuff you need that Apple or your Linux system didn’t.  
[See list of all packages](https://formulae.brew.sh/formula/)

	⁃	BREW package definition files are called “formulae”
	⁃	BREW “cask”, just like a formula, is for GUI installs.
	⁃	BREW “cellar” is where everything is installed /usr/local/Cellar


The simplest way to create a formula for your own software is to create a GitHub repository called homebrew-<something>; put your formula file in it; then type brew tap <username>/<something> to add this new source of formulae to your Homebrew installation and so get access to all its formulae.

Companies have internal Homebrew taps for their own utilities. There are a lot of public taps like homebrew/science for scientific software, atlassian/tap for Atlassian software, and ska-sa/tap for radio astronomy.

**[Brew Formulae / Casks](https://formulae.brew.sh/)**

## What is CHOCOLATEY?

For Windows

Chocolatey has the largest online registry of Windows packages. Chocolatey packages encapsulate everything required to manage a particular piece of software into one deployment artifact by wrapping installers, executables, zips, and/or scripts into a compiled package file.

[Search all Chocolatey Packages](https://chocolatey.org/packages)

- - -

Copyright © 2020 Qualex Consulting Services Incorporated.