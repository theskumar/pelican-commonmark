# CommonMark for Pelican

[![Build Status](https://travis-ci.org/theskumar/pelican-commonmark.svg)](https://travis-ci.org/theskumar/pelican-commonmark) [![Coverage Status](https://coveralls.io/repos/theskumar/pelican-commonmark/badge.svg)](https://coveralls.io/r/theskumar/pelican-commonmark)

This reader plugin replaces the markdown reader with one that uses the
[Python parser for CommonMark][1].

It is useful if you want to use the [CommonMark][2] way of parsing markdown
inside non-trivial nested HTML tags. It is not useful if you want to
use the extensions available to the python markdown parser.

## Installation

    pip install pelican-commonmark

Add/update the `PLUGINS` variable in your `pelicanconf.py`:

```
PLUGINS = [
    ...
    "pelican_commonmark",
    ...
]
```

## LICENSE

BSD

[1]: https://pypi.python.org/pypi/CommonMark
[2]: http://commonmark.org
