# ctf-finder



## it will work on:
- zip file
- file that will only work in the webshell or another Linux computer.
- binary: static

- server
- web url


# usage:

## m-file.py:
- ` python3 m-file.py 2>/dev/null`
- Upload file

## m-server.py:
- ` python3 m-server.py 2>/dev/null`
- Example use Like>(nc or ncat) : ` Host:jupiter.challenges.picoctf.org Port: 41120 `

## m-web.py:
- ` python3 m-web.py 2>/dev/null`
- Example : URL: ` https://jupiter.challenges.picoctf.org/problem/9670/ `

## m-ssh.py:
- ` python3 m-ssh.py 2>/dev/null`
- Example : `ssh ctf-player@venus.picoctf.net -p 60112`
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
