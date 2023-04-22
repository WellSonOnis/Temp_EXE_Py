Description
===========


`Temp_EXE_Py` is a simple Python script that use pyserial library to connect Arduino board to serial with nice GUI and Windows executable file .
`Python Serial Port Extension` for Win32, OSX, Linux, BSD, Jython, IronPython.

`pandas` is a Python package that provides fast, flexible, and expressive data structures designed to make working with "relational" or "labeled" data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real world data analysis in Python. Additionally, it has the broader goal of becoming the most powerful and flexible open source data analysis / manipulation tool available in any language. It is already well on its way towards this goal.


Installation
------------

 to install `pyserial`:

* With pip (preferred), run `pip install pyserial`.

to install `PIL`:

* With pip (preferred), run `pip install Pillow`.

to install `pandas`:

* With pip (preferred), run `pip install pandas`.

to install `matplotlib`:

* With pip (preferred), run `pip install matplotlib`.

to install `openpyxl`:

* With pip (preferred), run `pip install openpyxl`.


Usage
-----

Just copy all fils to your director and plug in your `Arduino` board (UNO) with Temperature sensor like LM35 Refer to the rest you can find YouTube linke to follow [the video](https://youtu.be/4D1jQvWOPrY) .

Note : make sure you are send temperature data in the Arduino code only (value) without any edition see my code `Temp.ino`.

the first line it important for starting:

```ipython
>>> import serial
```

Second, is for knowing the port that you are connected without human interaction:

```ipython
>>> import serial.tools.list_ports
```

That's it!


The librarys also contains a (currently undocumented) .

Contributing
------------

If you'd like to contribute to the code, thank you! To install the various libraries
required, run (preferably in a virtualenv):

```bash
$ pip install requirements.txt
```



Thanks again!

License
-------

`Temp_EXE_Py` is distributed under the MIT license.
## Author

- [ENPC](https://enp-constantine.dz)
- [Chokri Azzouzi](https://www.facebook.com/profile.php?id=100090514185128&mibextid=ZbWKwL)
- [Me](https://github.com/WellSonOnis)
- 
&copy; 2023 ENPC All Rights Reserved

# Changelog


## v3 (2023-03-02)

### Features

* Add "excel" model 

### Fixes

* Asynchronous of plotting 10 value of temperature





