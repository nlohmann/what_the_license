What The License!?
------------------

A tool to find the concrete open source licens given a source file header::

    >>> import what_the_license
    >>> what_the_license.wtk(open('some_source_file'))
	[
	  {
	    "score": 100.0, 
	    "license": "The MIT License"
	  }, 
	  {
	    "score": 48.030888030888036, 
	    "license": "Boost Software License - Version 1.0 - August 17th, 2003"
	  }, 
	  {
	    "score": 44.86486486486486, 
	    "license": "MOZILLA PUBLIC LICENSE Version 1.0"
	  }
	]
