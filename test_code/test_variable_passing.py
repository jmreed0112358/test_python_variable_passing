class class1(object):
	def __init__(self, dictionary):
		self.dictionary = dictionary

	def function1(self):
		self.dictionary['foo'] = 'foo'

class class2(object):
	def __init__(self, dictionary):
		self.dictionary = dictionary

	def function2(self):
		self.dictionary['foo'] = 'oof'


def function3(dictionary):
	dictionary['foo'] = 'welp'

# create a dict, and initialize it
thing = {}
thing['foo'] = 'bar'

# initial state.
test1 = class1(thing)
test2 = class2(thing)
print '\n'
print '-' * 10
print "thing.get(\'foo\'): %s" % thing.get('foo')
print "test1.dictionary.get(\'foo\') %s" % test1.dictionary.get('foo')
print "test2.dictionary.get(\'foo\') %s" % test2.dictionary.get('foo')

# start screwing around.
test1.function1()
print '\n'
print '-' * 10
print "thing.get(\'foo\'): %s" % thing.get('foo')
print "test1.dictionary.get(\'foo\') %s" % test1.dictionary.get('foo')
print "test2.dictionary.get(\'foo\') %s" % test2.dictionary.get('foo')

function3(thing)
print '\n'
print '-' * 10
print "thing.get(\'foo\'): %s" % thing.get('foo')
print "test1.dictionary.get(\'foo\') %s" % test1.dictionary.get('foo')
print "test2.dictionary.get(\'foo\') %s" % test2.dictionary.get('foo')

# screw around a little more.
print '\n'
print '-' * 10
test2.function2()
print "thing.get(\'foo\'): %s" % thing.get('foo')
print "test1.dictionary.get(\'foo\') %s" % test1.dictionary.get('foo')
print "test2.dictionary.get(\'foo\') %s" % test2.dictionary.get('foo')