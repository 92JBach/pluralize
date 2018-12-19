'''The MIT License

Copyright (c) 2010-2018 Google, Inc. http://angularjs.org

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
THE SOFTWARE.'''

class Plural:
    __slots__ = 'word', 'value', 'singular', 'plural', 'zero', 'ignore_negatives'

    def __init__(self, value: int, word: str = "", **kwargs):
        """
        Parameters
        ----------
        value : int
            The determining value
        word : str, optional
            The word to make plural. (defaults to "")
        singular : str, optional
            Appended to `word` if `value` == 1. (defaults to '')
        plural : str, optional
            Appended to `word` if `value` > 1. (defaults to 's')
        zero : str, optional
            Replaces `value` if `value` == 0. (defaults to 0)
        ignore_negatives : bool, optional
            This will raise ValueError if `value` is negative. (defaults to False)
            Set to True if you don't care about negative values.
        """

        self.value, self.word = value, word
        self.singular = kwargs.pop('singular', '')
        self.plural = kwargs.pop('plural', 's')
        self.zero = kwargs.pop('zero', 0)
        self.ignore_negatives = kwargs.pop('ignore_negatives', False)

    def __str__(self):
        v = self.value
        pluralizer = self.plural if abs(v) > 1 else self.singular

        if v < 0 and not self.ignore_negatives:
            raise ValueError

        return f"{v or self.zero} {self.word}{pluralizer}"
