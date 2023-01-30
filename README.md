# jupyter-notebook-m2
Dockerized jupyter notebook with VS Code and M2 GPU support. Requires M1/M2 based CPU.

__NOTE:__ M1/M2 GPU is NOT yet supported. For now, CPU only.

Build docker image:
---

```
$ docker build -f Dockerfile -t local/jupyternotebookm2:latest .
```

Create and run docker container:
---

```
$ docker compose up -d
```

Run VS Code inside docker container
---

1. Open VS Code workspace
2. (optional) Add ports forwarding of 8888 and 8889 in VS Code (for Juypter Notebook web app)
3. Dev Containers: Reopen in Container
4. Install VS Code extensions as needed