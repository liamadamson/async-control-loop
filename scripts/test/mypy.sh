# To be run from the main folder.

docker run --rm -it -v "$PWD":"/code/" async-control-loop mypy --strict ./src/