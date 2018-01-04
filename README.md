# grpc-Python-sample

## Description

- This is grpc server / client sample for Python.

## HOW TO USE

### INSTALL

```bash
$ git clone https://github.com/airking05/grpc-python-sample

$ cd grpc-python-sample

$ pip install -r requirements.txt

$ make build```
### Use

#### in one terminal

```bash
$ python protos/server.py```

#### in the other terminal
  
```bash
$ python protos/client.py

----- client is sending Ping to server -----
hage: "me too"
------------- response returned ------------

----- client is sending Ding to server -----
(Empty)
------------- response returned ------------```
