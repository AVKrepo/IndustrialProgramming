docker build . -t producer
docker run --net task0_default -it --rm producer
