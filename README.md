
# bitsbehumble

BitsBeHumble is a lightweight type converter python library. it is designed to make CTF scripting a wee bit easier.
Its main purpose is to save you the googling time you spend every time you need to convert from one type to another, convert endianness or simply convert a binary array to a binary string.

It doesn't support unicode, yet.

```python
>>> string_to_hex('Hello World!',end='little')
>>> 0x21646c726f57206f6c6c6548

>>> binary_to_string('0100100001100101011011000110110001101111')
>>> Hello

>>> little_to_big_endian(0x21646c726f57206f6c6c6548)
>>> 0x48656c6c6f20576f726c6421

>>> hex_to_binary('0x48656c6c6f20576f726c64',ret='list')
>>> ['0b1001000', '0b1100101', '0b1101100', '0b1101100', '0b1101111', '0b100000', '0b1010111', '0b1101111', '0b1110010', '0b1101100', '0b1100100']
```
---

# Installation

```pip install bitsbehumble```

---
# Contribution

Pull requests , Ideas  and feedback are welcomed.
 
# Documentation

Naming convetion: ```type_to_type()```.

Default return type: same type as the first argument unless specified otherwise.

Available return types :```ret='list', ret='int' , ret='str'```.

Default Endianness: big-endian 
Available Endianness: ``` end='big' , end='little' ```

All functions accept all 3 types of arguments ( int, str, list ) with or without prefixes ('0x' , '0b') unless specified otherwise in the function name, for example:

```python
binstr_to_binarray(bin_str)  
binarray_to_binstr(bin_arr)
string_to_binary(string, ret='default')
hexstring_to_array(hex_str)
hexarr_to_hexstring(hex_array)
string_to_hex(string ,end='big',ret='str') 
```
---
### Available Functions

```python
hex_to_binary(hx,ret='default')
```
params: ``` hx(any type)```
         ``` ret (str)```: 'int', 'str' or 'list'
         
default return type: (same as hx)  

```python
binary_to_hex(b,ret='default')
```
params: ```b (any type) ```
         ``` ret (str)```: 'int', 'str' or 'list'
         
default return type: (same as b)  

```python
hex_to_string(hx)
```
can also be called like this: ```unhexlify(hx)```
params: ```hx (any type) ``` 

default return type: (str)

```python
binary_to_string(b):
```
params: ```b (any type)```

default return type: (str)

```python
string_to_binary(string, ret='default')
```
params: ``` string (str)```
         ``` ret (str)```: 'int', 'str' or 'list'
         
default return type: (same as string)   

```python
string_to_hex(string ,end='big',ret='str')
```
can also be called like this: ```hexlify(string ,end='big',ret='str')```

params: ``` string (str)```
        ```end (str) ```: 'big' or 'little'
        ``` ret (str)```: 'int', 'str' or 'list'
            
            
default return type: (str)

```python

little_to_big_endian(hx,ret='default')
```
params: ``` hx (any type)```
          ``` ret (str)```: 'int', 'str' or 'list'

default return type: (same as hx)   

```python
big_to_little_endian(hx,ret='default')
```
params: ``` hx (any type)```
          ``` ret (str)```: 'int', 'str' or 'list'
          
default return type: (same as hx)   

```python
zero_extend(b,n,at='start')
```
works like python's zfill. 

for binary strings: extends them to a length divisible by 8 if (n) isn't specified.
if n is specified it adds (n) zeros to the start or the end of the string.
 
for strings: does nothing if (n) isn't specified.
if n is specified it adds (n) zeros to the start or the end of the string.

params: ```b (string) ```
``` n (int) ```
```at (str)```  'start' or 'end'

default return type:  (string)

```python
hexarr_to_hexstring(hex_array)
```
params: ```hex_array (list) ```

default return type: (str)

```python
binstr_to_binarray(bin_str)
```
params: ```bin_str (str) ```

default return type: (list)

```python
binarray_to_binstr(bin_arr)
```
params: ```bin_arr (list) ```

default return type: (str)

```python
to_binstr(b)
```
takes a binary of any type and returns a binary string

params: ```b (any type)```

default return type: (str)

```python
string_to_bytes(string,ret='default')
```
params: ``` string (str)```
         ``` ret (str)```: 'int', 'str' or 'list'
   
default return type: (same as string)      

```python
bytes_to_string(b)
```
params: ```b (any type) ``` : str , int , bytes, bytearray or list of any type.

default return type: (str)

```python
hexstring_to_array(hex_str):
```
params: ```hex_str (string) ```

default return type: (list)
```python
to_hexstr(hx)
```
takes a hex int/str/bytes/list/bytearray and returns the string representation of it

params: ``` hx (any type)```

default return type: (str)
```python
hex_to_bytes(hx)
```
params: ``` hx (any type)```

default return type: (bytes)

```python
is_valid_hex(hx)
```
params: ```hx (any type) ```

default return type: (bool)

```python
is_valid_binary(b)
```
params: ```b (any type) ```

default return type: (bool)

```python
getKey(dct,value)
```
searches a given dictionary for the key of the given value and returns a list of one or more keys

params: ```dct (dict) ```
		``` value (any type) ```
		
default return type: (list)
