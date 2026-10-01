#!/usr/bin/env bash
docker rmi $(docker images -a|grep "<none>"|awk '$1=="<none>" {print $3}')
