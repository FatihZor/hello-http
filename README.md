# hello-http
hello-http is a project built with flask for tests.

<p align="center"> <a href="https://hub.docker.com/r/fatihzor/hello-http" target="blank"><img src="https://img.shields.io/docker/pulls/fatihzor/hello-http.svg?style=for-the-badge&logo=docker" alt="fatihzor/hello-http" /></a> </p>

## basic run

```sh
docker run fatihzor/hello-http
```

## run with environments

```sh
docker run -e MESSAGE=test fatihzor/hello-http
```

```sh
docker run -e PORT=5005 -p 5005:5005 fatihzor/hello-http
```

## supported environment variables

| variable | description | default | example |
|----------|-------------|---------|---------|
| DEBUG | _ | False | DEBUG=True |
| HOST | _ | 0.0.0.0 | HOST=127.0.0.1 |
| PORT | _ | 5000 | PORT=5005 |
| MESSAGE | _ | Hello World! | MESSAGE=test |

