
class Name(object):

    def __init__(self,txt):
	self.name = txt

    def __str__(self):
	return self.name

if __name__ == '__main__':
    print('dummy guy was here!')
else:
    print(__name__)

