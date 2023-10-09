# ctf-finder

## m-file.py:
 ``` 
 python3 m-file.py 2>/dev/null
 ```
- Upload file
### Like: 
- zip file
- file that will only work in the webshell or another Linux computer.
- binary: static
- strings(check files without running them)

## m-server.py:
  ```
  python3 m-server.py 2>/dev/null 
  ```
- Example use Like>(nc or ncat) : ``` Host:jupiter.challenges.picoctf.org Port: 41120 ```

## m-web.py:
  ``` 
  python3 m-web.py 2>/dev/null
  ```
- Example : URL: ``` https://jupiter.challenges.picoctf.org/problem/9670/ ```

## m-ssh.py:
  ```
  python3 m-ssh.py 2>/dev/null
  ```
- Example : ``` ssh ctf-player@venus.picoctf.net -p 60112 ```
- Remote server hostname or IP address (venus.picoctf.net).
- Username (ctf-player).
- Port number (60112).
- for testing i n the file :
    ```
    hostname = "venus.picoctf.net"
    port = 60112
    username = "ctf-player"
    password = "6d448c9c"
    ```

## hexadecimal To ASCII(letters):
```
python3 m-hex.py 2>/dev/null
```
-  0x70 = p

## decimal_to_binary.py:
```
python3 m-dec_b 2>/dev/null
```
-  number 42 (base 10) = binary(base 2) 101010

## m-hash.py:
```
python3 m-dec_b 2>/dev/null
```
- Enter the URL: http://saturn.picoctf.net:50920/admin.php
- Enter the hash value: 2196812e91c29df34f5e217cfd639881
- CTF{j5_15_7r4n5p4r3n7_05df90c8}