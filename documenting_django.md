Source

Documenting your Django application with sphinx
 

Documenting web applications is not easy, over the last 8 years or so I have been a software consultant this has been one of the most challenging bits.

Overtime I have come to appreciate the value and importance of writing documentation, I setup my projects from the start to have documentation and thankfully with Django this is super easy.

After trying out a couple of  options and pulling out my hair in frustration smiley , I’ve settled with a combination of sphinx and django-docs which I’ve found to be both efficient , time saving and most importantly this setup fits naturally into my development flow, I don’t have to learn new markups or syntax to write my documentation, I simply use python docstrings and I am good to go.

For me documentation has two main benefits, it helps me understand my code better and helps others understand my code and thought process.With those benefits in mind let’s get started.

Install Sphinx
Sphinx is a document generator written in python, it was originally created to build the new Python documentation.
Sphinx converts reStructuredText files into HTML websites and other formats including PDF, EPub and man.

We will use pip to install Sphinx

$ pip install sphinx
Once the installation is done you will need to create the document root folder, this folder will hold  the generated documentation and also all the assets you will need to generate your documentation.Run the following command

$ sphinx-quickstart
You will be asked a number of questions.
This folder confiruation will create a docs folder inside my dev folder, containing the files conf.py, index.rst and Makefile, and the folders _build, _static and _templates (which will be empty).
You will need the autodoc option if you want to generate documentation from your python docstings

Welcome to the Sphinx 1.3.1 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Enter the root path for documentation.
> Root path for the documentation [.]: ./docs

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]: n

Inside the root directory, two more directories will be created; "_templates"
for custom HTML templates and "_static" for custom stylesheets and other static
files. You can enter another prefix (such as ".") to replace the underscore.
> Name prefix for templates and static dir [_]: _

The project name will occur in several places in the built documentation.
> Project name: dev
> Author name(s): Madra David

Sphinx has the notion of a "version" and a "release" for the
software. Each version can have multiple releases. For example, for
Python the version is something like 2.5 or 3.0, while the release is
something like 2.5.1 or 3.0a1.  If you dont need this dual structure,
just set both to the same value.
> Project version: 0.1
> Project release [0.1]: 0.1

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
http://sphinx-doc.org/config.html#confval-language.
> Project language [en]: en

The file name suffix for source files. Commonly, this is either ".txt"
or ".rst".  Only files with this suffix are considered documents.
> Source file suffix [.rst]: .rst

One document is special in that it is considered the top node of the
"contents tree", that is, it is the root of the hierarchical structure
of the documents. Normally, this is "index", but if your "index"
document is a custom template, you can also set this to another filename.
> Name of your master document (without suffix) [index]: index

Sphinx can also add configuration for epub output:
> Do you want to use the epub builder (y/n) [n]: n

Please indicate if you want to use one of the following Sphinx extensions:
**_> autodoc: automatically insert docstrings from modules (y/n) [n]: y_**
> doctest: automatically test code snippets in doctest blocks (y/n) [n]: y
> intersphinx: link between Sphinx documentation of different projects (y/n) [n]: y
> todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: y
> coverage: checks for documentation coverage (y/n) [n]: y
> pngmath: include math, rendered as PNG images (y/n) [n]: y
> mathjax: include math, rendered in the browser by MathJax (y/n) [n]: n
> ifconfig: conditional inclusion of content based on config values (y/n) [n]: n
> viewcode: include links to the source code of documented Python objects (y/n) [n]: n

A Makefile and a Windows command file can be generated for you so that you
only have to run e.g. `make html` instead of invoking sphinx-build
directly.
_**> Create Makefile? (y/n) [y]: y **_
> Create Windows command file? (y/n) [y]: n

Creating file .docs/conf.py.
Creating file .docs/index.rst.
Creating file .docs/Makefile.

Finished: An initial directory structure has been created.

You should now populate your master file .docs/index.rst and create other documentation
source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
Two options in particular standout, you will need to select y when you reach them.

$ > autodoc: automatically insert docstrings from modules (y/n) [n]: y

$ > Create Makefile? (y/n) [y]: y 
By now you should have a /docs folder in your application directory.

Build the HTML files
Time for the nice part smiley. 

To build the html files you will to cd into your** /docs **folder and hit the make command.

$ make html
The make command will generate html files inside _build/ directory . The output of that command should be something like this

sphinx-build -b html -d _build/doctrees   . _build/html
Running Sphinx v1.3.1
making output directory...
loading pickled environment... not yet created
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 1 source files that are out of date
updating environment: 1 added, 0 changed, 0 removed
reading sources... [100%] index                                                                                                                 
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [100%] index                                                                                                                  
generating indices... genindex
writing additional pages... search
copying static files... done
copying extra files... done
dumping search index in English (code: en) ... done
dumping object inventory... done
build succeeded.

Build finished. The HTML pages are in _build/html.
 

Configure Sphinx
You have not yet configured Sphinx to fetch documentation from your project , to do this you will need to edit the** /docs/conf.py** file. 

After the line

import os

add this

sys.path.insert(0, os.path.abspath('..'))
from django.conf import settings
settings.configure()
This configures Sphinx to look inside your project folder for docstrings.
Inside your /docs folder add a modules folder to hold your_ documentation , _for example add a views.rst file to hold your views documentation

$ mkdir modules
$ touch modules/views.rst
Edit modules/views.rst and add the following

Views
======
.. automodule:: yourproject.yourapp.views
    :members:
Sphinx (autodoc) will now look for through the views.py file in your project.yourapp folder for doc-strings.

Finally you will need to include this documentation in your index.rst file, add this

Contents:
.. toctree::
   :maxdepth: 2

   modules/views
Once you’ve done that go ahead and build the documentation

$ make html
Your documentation is now inside the build folder, take a look at your _build/html/index.html file.

Congratulations smiley !

You can now start documenting your Django application.
