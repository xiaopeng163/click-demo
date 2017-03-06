# click-demo

```
$ cd click-demo
$ python setup.py install
$ clickctl
Usage: clickctl [OPTIONS] COMMAND [ARGS]...

  Click Demo Command Line Interface

Options:
  -v, --verbose  show debug message.
  --help         Show this message and exit.

Commands:
  init    Initializes a controller cluster on master node.
  join    join the controller cluster as agent node
  status  Get cluster node list
$ clickctl init --help
Usage: clickctl init [OPTIONS]

Options:
  --advertise-addr TEXT  The REST Server advertise address  [required]
  --help                 Show this message and exit.

$ clickctl init --advertise-addr=1.1.1.1:80
Try to initialized the cluster
$ clickctl -v init --advertise-addr=1.1.1.1:80
Try to initialized the cluster
The REST Server advertise address: 1.1.1.1:80
```