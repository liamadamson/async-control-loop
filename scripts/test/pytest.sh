# To be run from the main folder.

docker run --rm -it -v "$PWD/src":"/code/src" -v "$PWD/test":"/code/test" async-control-loop pytest ./test/