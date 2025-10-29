from src.dsa.queue import Queue

q = Queue(["a","b","c"])

def test_enqueue():
	q.enq("d")
	assert q.elements == ["a", "b", "c", "d"]
	assert q.size() == 4

def test_dequeue():
	el = q.deq()
	assert q.elements == ["b", "c", "d"] and el == "a"
	q.deq() # b
	q.deq() # c
	assert q.peek() == "d"
	q.deq() # d
	assert q.empty() == True