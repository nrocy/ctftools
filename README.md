CTF Tools
=========

Often when doing CTFs I need a encode or decode strings between formats,
inspect HTTP headers, and other such things. Instead of going to websites
to do this (there's plenty to do that), I decided to write a small
toolset for myself. 

Usage
-----

Start it with `ctf.py` and you will see a prompt.

    ctf] 

 typing `help` brings up the help. 

 To make use of a module (I will add more over time), for example the `codecs`
 tools:

    ctf] codecs
    ctf:codecs] 

 Now you are in the `codecs` module which is used to encode and decode
 strings. For example:

    ctf:codecs] b64 enc testing this thing
    dGVzdGluZyB0aGlzIHRoaW5n
    ctf:codecs]

The `_` will always be replaced by the last output:

    ctf:codecs] b64 dec _
    testing this thing
    ctf:codecs]

 `help` also works here.

TODO
----

Lots, so sit tight, or suggest some things. Right now some things that
are planned are:

* HTTP header inspection
* Basic encryption (caesar, voignere, etc)
* whatever else I find I need

License
-------

The MIT License (MIT)

Copyright (c) <2015> <Sven Steinbauer>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
