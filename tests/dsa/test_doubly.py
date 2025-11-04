import pytest
from src.dsa.doubly import *

d = Doubly()
d.prepend("f")
d.prepend("e")
d.prepend("d")
d.prepend("c")
d.prepend("b")
d.prepend("a")

def test_prepend():
	assert str(d) == 'a <-> b <-> c <-> d <-> e <-> f'

def test_append():
	d.append("g")
	assert str(d) == 'a <-> b <-> c <-> d <-> e <-> f <-> g'

def test_put():
	d.put("x", 2)
	assert str(d) == 'a <-> x <-> b <-> c <-> d <-> e <-> f <-> g'

def test_backward():
	assert d.backward() == 'g <- f <- e <- d <- c <- b <- x <- a'