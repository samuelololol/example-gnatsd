## Deployment

pynats-pub -> gnats("foo" topic) <-pynats-sub

* [pynats](https://github.com/mcuadros/pynats)
* [gnatsd](https://github.com/nats-io/gnatsd)


## Requirement

* docker
* docker-compose

## Run (broadcast)

```
$ docker-compose up -d
Creating examplegnatsd_gnatsd_1...
Creating examplegnatsd_stone_1...
Creating examplegnatsd_pynatss1_1...
Creating examplegnatsd_pynatss2_1...
Creating examplegnatsd_pynatsp_1...

$ docker logs -f
examplegnatsd_pynatss1_1             
waiting for 1 msg
Received a message: Hello World!
received 1 msg

$ docker logs -f
examplegnatsd_pynatss2_1
waiting for 1 msg
Received a message: Hello World!
received 1 msg

```
