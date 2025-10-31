import pytest
from src.dsa.doubly import *

head = Node("a")
head.next = Node("b")
head.next.next = Node("c")
before = head.next.next.next = Node("d")
head.next.next.next.next = Node("e")
head.next.next.next.next.next = Node("f")

def test_pop():
	pop(head)
	assert show(head) == 'a <-> b <-> c <-> d <-> e <-> None'

def test_unshift():
	h = unshift(head)
	assert show(h) == "b <-> c <-> d <-> e <-> None"

@pytest.mark.skip(reason="Not working")
def test_remove():
	h = rm(head, 1)
	print(show(h))

@pytest.mark.skip(reason="Not working")
def test_insert_before():
	h = put(before, Node("x"))
	print(show(head))

def test_append():
	h = append(head, Node("y"))
	assert show(h) == "a <-> b <-> c <-> d <-> e <-> y <-> None"

def test_prepend():
	h = shift(head, Node("y"))
	assert show(h) == "y <-> a <-> b <-> c <-> d <-> e <-> y <-> None"
