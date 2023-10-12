# ctf-finder

## m-file.py:
 ``` 
 python3 m-file.py 
 ```
- Upload file
### Like: 
- zip file
- file that will only work in the webshell or another Linux computer.
- binary: static
- strings(check files without running them)

## m-server.py:
  ```
  python3 m-server.py  
  ```
- Example use Like>(nc or ncat) : ``` Host:jupiter.challenges.picoctf.org Port: 41120 ```

## m-web.py:
  ``` 
  python3 m-web.py 
  ```
- Example : URL: ``` https://jupiter.challenges.picoctf.org/problem/9670/ ```

## m-ssh.py:
  ```
  python3 m-ssh.py 
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
python3 m-hex.py 
```
-  0x70 = p

## decimal_to_binary.py:
```
python3 m-dec_b 
```
-  number 42 (base 10) = binary(base 2) 101010

## m-hash.py:
```
python3 m-dec_b 
```
- Enter the URL: http://saturn.picoctf.net:50920/admin.php
- Enter the hash value: 2196812e91c29df34f5e217cfd639881
- CTF{j5_15_7r4n5p4r3n7_05df90c8}

## m-crypto.py:
```
python3 m-crypto.py
```
- EX:
```
 cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_MAZyqFQj}
```
## m-rsa_decrypt(RSA):
```
python3 m-rsa_decrypt.py
```
- Enter c,n,e
- EX:
- C:
```
 62324783949134119159408816513334912534343517300880137691662780895409992760262021
```
- N:
```
 1280678415822214057864524798453297819181910621573945477544758171055968245116423923
```
- E:
```
 65537
```

## m-mysql(postgresql-sql)[show all tables & print CTF]:

```
brew install postgresql@14

```
```
python3 m-mysql.py
```

- Enter :
- Host(saturn.picoctf.net) , Port(59244), Username(postgres), Password(postgres), Database(name(pico))
- EX: `psql -h saturn.picoctf.net -p 59244 -U postgres pico`
- `Password is postgres`

## using terminal:
- Connect to database:
 ```
 psql -h your_host -p your_port -U your_username -d your_database

```
- Once connected to the database, you can list all the tables in the current database using the following SQL command:
```
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;
```
-  enable expanded display mode by entering the following command:

```
\x
```
- data from a specific table, replacing your_table with the name of the table you want to query:
```
SELECT * FROM your_table;
```
## m-nc.py (to not use nc):

```
python3 m-nc.py 
```
- Need: file , Host , Port


