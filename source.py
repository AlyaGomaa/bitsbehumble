
def zero_extend(bin_str):
	bin_str = bin_str.replace('0x','')
	b= bin_str
	if len(bin_str) % 8 != 0:
		padding=''
		while( len(bin_str) % 8 != 0 ):
			padding += '0'
			bin_str = padding + b

	return bin_str


def is_valid_hex(hx):
	cases = {
		int: hex,
		str: str,
		list: ''.join
		}
	
	if type(hx) not in cases:
		raise TypeError('Unsupported hex input!')
	
	try:
		int(cases[type(hx)](hx), 16)
		return True
	except:
		return False


def is_invalid_binary(b):
	b=b.replace('0x','')
	if(len(b) %8 != 0):
			return True
	else:
		return False


def default_return_type(arg,return_type):
	global ret ,type_
	ret= return_type
	type_ = type(arg)
	if(ret == 'default'): 
		if type_==list: ret = 'list'
		elif type_ == str: ret = 'str' 
		elif type_ == int: ret = 'int' 
	return ret


def invalid_return_type():
	raise Exception("Valid return types are either 'int', 'str' or 'list'.")


def string_to_bytes(string,ret='default'):

	assert( type(string) == str ) ,'Invalid type'
	ret = default_return_type(string,ret) 

	if(ret=='str'):
		return bytes(string,'utf-8')
	else: # list or int
		return [ ord(char) for char in string] 


def string_to_binary(string, ret='default'): 
	assert( type(string) == str ) ,'Invalid type'
	ret = default_return_type(string,ret)	
	if(string.startswith('0x')): 
		string = string[2:]
		string = hex_to_string(string)

	bin_arr=[]
	for char in string:
		bin_char = bin(ord(char)).replace('0b','').zfill(8)
		bin_arr.append(bin_char)

	bin_str = ''.join(bin_arr)
	if(ret=='str'):
		return bin_str
	elif(ret=='list'):
		bin_arr= [bin(int(char,2)) for char in bin_arr]
		return bin_arr
	elif(ret=='int'):
		return '0b' + bin_str
	else:
		invalid_return_type()


def hexstring_to_array(hex_str):
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
	string= ''.join([hex(ord(c))[2:].zfill(2) for c in string])
	hex_str = string

	if(end=='little'):
		hex_str_l='0x'
		string=string[::-1]
		for i in range(1,len(string),2):
			byte =  string[i] + string[i-1]
			hex_str_l+=  byte
		hex_str = hex_str_l
	elif(end=='big'):
		hex_str ='0x' + hex_str


	if(ret=='str' or ret=='int'):
		return hex_str

	elif(ret=='list'):
		return hexstring_to_array(hex_str)
	else:
		invalid_return_type()

hexlify = string_to_hex


def little_to_big_endian(hx,ret='default'): 
	assert is_valid_hex(hx),'Invalid Hex.'
	ret = default_return_type(hx,ret)

	if(type_ == int):
		hex_str = str(hex(hx))[2:]
	elif(type_ == str ):
		hex_str = hx
		if hex_str.startswith('0x'):
			hex_str=hx[2:]
	elif(type_ == list):		
		hex_str =''.join(hx).replace('0x','')

	hex_str=hex_str[::-1]
	s='0x'
	for i in range(1,len(hex_str),2):
		s+= hex_str[i] + hex_str[i-1]
	if(len(s[2:])!= len(hex_str)): #in case odd number of bytes was passed
		s+='0'+hex_str[-1]

	if(ret=='str' or ret=='int'): #hex ints are of type str
		return s
	elif(ret=='list'):
		return hexstring_to_array(s)
	else:
		invalid_return_type()

big_to_little_endian = little_to_big_endian #;D

def hex_to_bytes(hx):
	assert is_valid_hex(hx),'Invalid Hex.'
	if(type(hx) == list):
		hex_str = hexarr_to_hexstring(hx)[2:]
	elif(type(hx) == str ):
		hex_str = hx
		if hx.startswith('0x'):
			hex_str = hx[2:]
	elif(type(hx) == int):
		hex_str = str(hex(hx))[2:]

	return bytes.fromhex(hex_str)




def hex_to_string(hx):  
	assert is_valid_hex(hx),'Invalid Hex.'
	if(type(hx)==str): 
		hex_array =hexstring_to_array(hx)
		
	elif(type(hx)==int):
		hex_str =  str(hex(hx))
		hex_array = hexstring_to_array(hex_str)
	elif(type(hx) == list):
		hex_array = hx

	hex_array =  [int(hx,16) for hx in hex_array]
	string =  ''.join(map(chr,hex_array ))
	return string	

unhexlify=hex_to_string

def hexarr_to_hexstring(hex_array):
	assert(type(hex_array) == list) , 'Invalid type'
	assert is_valid_hex(hx),'Invalid Hex.'
	hex_str = ''.join(hex_array).replace('0x','')
	return '0x' + hex_str


def binstr_to_binarray(bin_str):
	assert(type(bin_str) == str) , 'Invalid type.'
	if(bin_str.startswith('0b')): 
		bin_str = bin_str.replace('0b','')

	if is_invalid_binary(bin_str):
		bin_str= zero_extend(bin_str)

	byte_array=[]
	for i in range(0,len(bin_str),8):
		byte=''
		for j in range(8):
			byte += bin_str[i+j]
		byte_array.append(bin(int(byte,2)))
	return byte_array


def binarray_to_binstr(bin_arr):
	assert(type(bin_arr) == list) , 'Invalid type'

	bin_str=''
	for byte in bin_arr:
		byte = byte.replace('0b','')
		if(is_invalid_binary(byte)):
			byte = zero_extend(byte)
		bin_str += byte

	return bin_str


def binary_to_string(b): 
	type_ = type(b)
	if( type_ == int):
		bin_str = str(bin(b)).replace('0b','')
		if is_invalid_binary(bin_str):
			bin_str= zero_extend(bin_str)
	elif(type_==str):
		bin_str=b.replace('0b','')
		if is_invalid_binary(bin_str):
			bin_str= zero_extend(bin_str)
	elif(type_ == list):
		bin_str = binarray_to_binstr(b)

	bin_arr = binstr_to_binarray(bin_str)
	string = ''
	for byte in bin_arr:
		string+= chr(int(byte,2))
	return string


def bytes_to_string(b): 
	type_ = type(b)
	if(type_ == list):
		
		bytes_arr=b
		type_ = type(bytes_arr[0])

		if(type_==int):
			string = ''.join(map(chr, bytes_arr))

		elif(type_==str): 
			string =  ''.join([chr(ord(byte)) for byte in bytes_arr])
		elif(type_ == bytes):
			bytes_string=''
			for byte in bytes_arr:
				bytes_string +=str(byte)
			return bytes_to_string(bytes_string)

	elif(type_ == bytes or type_ ==  bytearray or type_==str): 
		bytes_str = str(b)
		l=['bytearray(',')','b','\\x','"',"'"]
	
		for element in l:
				if(element in bytes_str): 
					bytes_str = bytes_str.replace(element,'')
		string = bytes_str
		
		if(is_valid_hex(string)):
			string=hex_to_string(string)

		elif( is_invalid_binary(string)):
			string = zero_extend(string)
			string = binary_to_string(string)
		else:
			string = binary_to_string(string)
		
		return string


def hex_to_binary(hx,ret='default'): 
	assert is_valid_hex(hx),'Invalid Hex.'
	ret = default_return_type(hx,ret)
	if(type(hx) == int):  
		hex_str = str(hex(hx))[2:]
	if(type(hx) ==  str ):
		hex_str = hx
		if(hx.startswith('0x')) : hex_str=hx[2:]

	bin_str=''
	for i in range(1,len(hex_str),2):
		byte= hex_str[i-1] + hex_str[i]
		byte = str(bin(int(byte,16))).replace('0b','').zfill(8)
		bin_str+= byte

	if(ret=='str'):
		return bin_str
	elif(ret=='list'):
		return binstr_to_binarray(bin_str)
	elif(ret=='int'):
		return '0b' + bin_str
	else:
		invalid_return_type()


def binary_to_hex(b,ret='default'): 
	ret = default_return_type(b,ret)

	if(type_ == int):
		bin_str = str(int(b,2)).replace('0x','')
	elif(type_ == list):
		bin_str = binarray_to_binstr(b)
	elif(type_ == str):
		bin_str = b.replace('0x','')

	bin_arr =binstr_to_binarray(bin_str)
	hex_array=[]
	for byte in bin_arr:
		byte=byte.replace('0b','')
		hex_array.append(hex(int(byte,2)))
	
	hex_str ='0x' + ''.join([byte[2:] for byte in hex_array])
	if(ret=='list'):
		return hex_array
	elif(ret == 'str'):
		return hex_str[2:]
	elif(ret == 'int'):
		return hex_str
	else:
		invalid_return_type()


#useless functions :D

int_to_bin = lambda i: bin(i)
bin_to_decimal = lambda b: int(b,2)
int_to_hex = lambda i: hex(i)
hex_to_decimal = lambda h: int(h,16)


#todo: suppport wide chars
