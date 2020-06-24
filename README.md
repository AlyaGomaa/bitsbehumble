# bitsbehumble

BitsBeHumble is a lightweight type converter python library. it is designed to make CTF scripting a wee bit easier.
Its main purpose is to save you the googling time you spend everytime you need to convert from one type to another, convert endianness or simply convert a binary array to a binary string.

It doesnt support unicode, yet.
Contribution and pull requests are welcomed.

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

Default default return type: same type as the first argument unless specified otherwise.

Available return types are:```ret='list', ret='int' , ret='str'```.

Default Endianness: big-endian 
Available Endianness: ``` end='big' , end='little' ```

All functions accept all 3 types of arguments ( int, str, list ) with or without prefixes ('0x' , '0b') unless specified otherwise in the function name, for example:

```python
binstr_to_binarray(bin_str)  
binarray_to_binstr(bin_arr)
zero_extend(bin_str)
is_valid_hex(hx)
is_invalid_binary(b)
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
zero_extend(bin_str)
```
works like python's zfill.

params: ```bin_str (string) ```

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
string_to_bytes(string,ret='default')
```
params: ``` string (str)```
         ``` ret (str)```: 'int', 'str' or 'list'
         
default return type: (same as string)      

```python
bytes_to_string(b)

```
params: ```b (any type) ``` str , int or bytes or list of any type

default return type: (str)

```python
hexstring_to_array(hex_str):
```
params: ```hex_str (string) ```

default return type: (list)

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
is_invalid_binary(b)
```
params: ```b (string) ```

default return type: (bool)
