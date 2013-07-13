from distutils.core import setup

classifiers = """\
Development Status :: 5 - Production/Stable
Environment :: Web Environment
Intended Audience :: Developers
License :: OSI Approved :: GNU General Public License (GPL)
Operating System :: OS Independent
Topic :: Internet :: WWW/HTTP
Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries
"""
import sys
if sys.version_info < (2, 3):
    _setup = setup
    def setup(**kwargs):
        if kwargs.has_key("classifiers"):
            del kwargs["classifiers"]
        _setup(**kwargs)

setup(name="cgi_app",py_modules=["cgi_app"],
        version="1.3",
        maintainer="Anders Pearson",
        maintainer_email="anders@columbia.edu",
        url = "http://thraxil.org/code/cgi_app/",
        license = "http://www.gnu.org/licenses/gpl.html",
        platforms = ["any"],
        description = "CGI and mod_python MVC application framework",
        long_description = """framework for building MVC CGI and mod_python
        applications. based on the perl CGI::Application module but more
        pythonic.""",
        classifiers = filter(None, classifiers.split("\n")))
