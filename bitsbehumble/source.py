def is_valid_hex(hx): 
	if type(hx) is list :
		for byte in hx:
			if(not is_valid_hex(byte)): return False
		return True
	else:
		cases = {
			int: hex,
			str: str,
			bytes: lambda b : "".join(map(chr,b )) , 
			bytearray: lambda b : "".join(map(chr,b ))  
			}
		
		if type(hx) not in cases:
			raise TypeError('Unsupported hex input.')

		try:
			int(cases[type(hx)](hx), 16)
			return True
		except:
			return False


def binarray_to_binstr(bin_arr):
	assert(type(bin_arr) is list) , 'Invalid type'
	bin_str=''
	for byte in bin_arr:
		byte = str(byte).replace('0b','').zfill(8)
		bin_str += byte
	return bin_str


def to_binstr(b): 
	#takes a binary of any type
	cases = {
		str:lambda b :  b ,
		int: str, 
		list:binarray_to_binstr,
		bytes: lambda b : b.decode('utf-8'),
		bytearray: lambda b : b.decode('utf-8'),
	}
	bin_str = cases [type(b)](b).replace('0b','')
	return bin_str


def is_valid_binary(b):
	
	bin_str = to_binstr(b)
	if any([b not in '01' for b in bin_str])==True :
		return False
	else:
		return True


def isnt_valid_bytes(b): #undocumented
	b = to_binstr(b)
	if(len(b) %8 != 0):
		return True
	return False

def zero_extend(b,n=0,at='start'):
	number_of_zeros = n
	b= to_binstr(b)
	if is_valid_binary(b) :
		
		bin_str = b
		if number_of_zeros : 
			return number_of_zeros*'0' + bin_str if at=='start' else bin_str + number_of_zeros*'0'
		
		b= bin_str
		if len(bin_str) % 8 != 0:
			padding=''
			while( len(bin_str) % 8 != 0 ):
				padding += '0'
				bin_str = padding + b

		return bin_str
	else: 
	#zero extend strings
		cases = {
			'start' :number_of_zeros*'0' + str(b),
			'end' : str (b) + number_of_zeros * '0' }
		return  cases[at] 


def default_return_type(arg,return_type):
	global ret ,type_
	ret= return_type
	cases = {
		list : 'list',
		str: 'str',
		int: 'int' 
	}
	if(ret == 'default'): 
		ret= cases[type(arg)]
	return ret



def invalid_return_type():
	raise TypeError("Valid return types are either 'int', 'str' or 'list'.")


def string_to_bytes(string,ret='default'):
	assert( type(string) == str ) ,'Invalid type'
	ret = default_return_type(string,ret) 
	return bytes(string,'utf-8') if ret=='str' else [ ord(char) for char in string] 


def string_to_binary(string, ret='default'):  
	assert( type(string) == str ) ,'Invalid type'
	ret = default_return_type(string,ret)	
	if string.startswith('0x') : 
		string = hex_to_string(string[2:])

	bin_arr=[]
	for char in string:
		bin_char = bin(ord(char)).replace('0b','').zfill(8)
		bin_arr.append(bin_char)
	bin_str = ''.join(bin_arr)

	cases = {
		'str':bin_str,
		'list': [bin(int(char,2)) for char in bin_arr],
		'int': '0b' + bin_str
	}
	try:
		return cases[ret]
	except:
		invalid_return_type()


def hexstring_to_array(hex_str):  # e.g "0xe56f" >> "['0xe5' , '0x6f']"
	assert(type(hex_str) == str) , 'Invalid type'
	if not hex_str.startswith('0x'): 
			hex_str='0x' + hex_str 
	if(' ' in hex_str):
		hex_array = hex_str.replace(' ', ' 0x').split()
	else: 
		hex_array=[]
		for i in range(3,len(hex_str),2):
			char = '0x' + hex_str[i-1] + hex_str[i]
			hex_array.append(char)
		
		if(len(hex_str)%2!=0): #in case sth like  ffe1254 was passed
			hex_array.append('0' + hex_str[2])
	return hex_array


def string_to_hex(string ,end='big',ret='str'):  
	assert(type(string) == str) , 'Invalid type'
	string= ''.join([hex(ord(c))[2:].zfill(2) for c in string.replace('0x','')])
	hex_str = string

	if end is 'little' :
		hex_str_l='0x'
		string=string[::-1]
		for i in range(1,len(string),2):
			byte =  string[i] + string[i-1]
			hex_str_l+=  byte
		hex_str = hex_str_l

	elif end=='big' :
		hex_str ='0x' + hex_str

	cases = {
		'str': hex_str,
		'int': hex_str,
		'list' : hexstring_to_array(hex_str)
	}
	try:
		return cases[ret]
	except:
		invalid_return_type()

hexlify = string_to_hex


def hexarr_to_hexstring(hex_array): 
	assert(type(hex_array) == list and is_valid_hex(hex_array)) , 'Invalid type'
	hex_str =   '0x' + ''.join(hex_array).replace('0x','')
	return  hex_str



def binstr_to_binarray(bin_str): 
	assert(type(bin_str) == str and is_valid_binary (bin_str)) , 'Invalid type.'

	bin_str = bin_str.replace('0b','')
	if isnt_valid_bytes(bin_str): #add leading zeros to make convesion possible
		bin_str= zero_extend(bin_str)

	byte_array=[]
	for i in range(0,len(bin_str),8):
		byte=''
		for j in range(8):
			byte += bin_str[i+j]
		byte = format(int(byte,2) , '#010b') #to keep the leading zeros
		byte_array.append(byte)

	return byte_array


def binary_to_string(b):  
	bin_str = to_binstr(b)
	assert( is_valid_binary (b))

	if isnt_valid_bytes(bin_str):
		bin_str= zero_extend(bin_str)

	bin_arr = binstr_to_binarray(bin_str)
	string = ''
	for byte in bin_arr:
		string+= chr(int(byte,2))
	return string


def hex_to_string(hx): 
	cases=[bytes,bytearray]
	if type(hx) in cases:
		return bytes_to_string(hx)

	assert is_valid_hex(hx)

	
	cases={
	str: lambda s: hexstring_to_array(s),
	int: lambda i: hexstring_to_array(str(hex(i))),
	list: list,
	}

	hex_array = cases[type(hx)](hx)
	hex_array =  [int(str(hx),16) for hx in hex_array]
	string =  ''.join(map(chr,hex_array ))
	return string	

unhexlify=hex_to_string


def bytes_to_string(b): 
	type_ = type(b)
	if(type_ == list):
		byte_arr=b
		type_ = type(byte_arr[0])
		cases={
			int: lambda i: ''.join(map(chr, i)) ,
			str: lambda s :  ''.join([chr(int(byte,16)) for byte in s]) if is_valid_hex(s) else 0 ,
			bytes: lambda b: hex_to_string(''.join([byte.decode('utf-8') for byte in b]).strip('0x','')),
			bytearray: lambda b: bytes_to_string(''.join([byte.decode('utf-8') for byte in b]))
		}
		string = cases[type(byte_arr[0])](byte_arr)
		return string
	else: 
		cases={ 
			int: lambda i: ''.join(map(chr, i)),
			bytes: lambda b: chr(int(b,16)), 
			bytearray: lambda b:''.join([chr(int(b,16)) for x in b]),
			str: hex_to_string
		}
		string = cases[type_](b)
		
		return string


def to_hexstr(hx): #takes hex only
 # undocumented
	cases = {
	int: lambda i :str(hex(i)),
	str: lambda s: '0' + s if len(s.replace('0x',''))==1 else s,
	bytes: lambda b : b.decode('utf-8') , 
	bytearray: lambda b : b.decode('utf-8')  ,
	list: lambda l : hexarr_to_hexstring([to_hexstr(hx) for hx in l])
	}

	hex_string = cases[type(hx)](hx).replace('0x','')
	return hex_string


def hex_to_bytes(hx): 
	assert is_valid_hex(hx)
	hex_str = to_hexstr(hx)
	return bytes.fromhex(hex_str)


def little_to_big_endian(hx,ret='default'): 
	assert is_valid_hex(hx)
	ret = default_return_type(hx,ret)

	hex_str = to_hexstr(hx).replace('0x','')[::-1]
	s='0x'

	for i in range(1,len(hex_str),2):
		s+= hex_str[i] + hex_str[i-1]

	if len(s[2:])!= len(hex_str): #in case odd number of bytes was passed
		s+='0'+hex_str[-1]

	cases = {
		'str':s ,
		'int': s , 
		'list': hexstring_to_array(s)
	}

	try:
		return cases[ret]
	except:
		invalid_return_type()
big_to_little_endian = little_to_big_endian #;D



def hex_to_binary(hx,ret='default'):
	assert is_valid_hex(hx)
	ret = default_return_type(hx,ret)
	hex_str = (to_hexstr(hx))

	bin_str=''
	for i in range(1,len(hex_str),2):
		byte= hex_str[i-1] + hex_str[i]
		byte = str(bin(int(byte,16))).replace('0b','').zfill(8)
		bin_str+= byte
	
	cases={
		'str':bin_str,
		'list': binstr_to_binarray(bin_str),
		'int': '0b' + bin_str
	}
	try :
		return cases[ret]
	except:
		invalid_return_type()


def binary_to_hex(b,ret='default'): 
	ret = default_return_type(b,ret)
	bin_str = to_binstr(b)

	bin_arr =binstr_to_binarray(bin_str)

	hex_array=[]
	for byte in bin_arr:
		hex_array.append(hex(int(byte,2)))

	hex_str= to_hexstr(hex_array)
	cases={
	'list':hex_array,
	'str':hex_str,
	'int': hex_str
	}
	try:
		return cases[ret]
	except:
		invalid_return_type()

#useless functions :D

int_to_bin = lambda i: bin(i)
bin_to_decimal = lambda b: int(b,2)
int_to_hex = lambda i: hex(i)
hex_to_decimal = lambda h: int(h,16)
def getKey(dct,value):
	return [key for key in dct if (dct[key] == value)]


#todo: suppport wide chars
