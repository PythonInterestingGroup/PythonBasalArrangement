
 
class Field(object): #用来保存数据库表的字段名和字段类型

	def  __init__(self, name, cloumn_type):
		self.name = name
		self.cloumn_type = cloumn_type

	def  __str__():
		return "<%s:%s>" % (self.__class__.__name__, self.name)

class StringField(Field):

	def __init__(self, name):
		super(StringField, self).__init__(name, 'varchar(100)')

class IntergerField(Field):

	def  __init__(self, name):
		super(IntergerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):

	def __new__(cls, name, bases, attrs):
		if name == 'Model':
			return type.__new__(cls, name, bases, attrs)
		print('Found model:%s'%name)
		mapping = dict()
		for k, v in attrs.items():
			if isinstance(v, Field):
				print("Found mapping: %s ==> %s" % (k, v))
				mapping[k] = v
		for k in mapping.keys():
			attrs.pop(k)
		attrs['__mappings__'] = mapping #保存属性和列的映射关系
		attrs['__table__'] = name #假设表明和类名一致
		return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):

	def __init__(self, **kw):
		super(Model,self).__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Model' object has no attribute '%s'" % key)
		
	def __setattr__(self, key, value):
		self[key] = value

	def save(self):
		fileds = []
		params = []
		args = []
		for k, v in self.__mappings__.items():	
			fileds.append(v.name)
			params.append('?')
			args.append(getattr(self, k, None))
		sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fileds),','.join(params))
		print('SQL %s'%sql)
		print('ARGS: %s'%str(args))

class User(Model):
	pass

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()

			