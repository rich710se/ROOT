# Development setup (docker based)

Dir structure:
```text
config (Home Assistant config dir)
backend (Backend files)
```

Clone backend to `backend` with `git clone git@github.com:ludeeus/home-assistant.git backend`

**Start the container:**

```shell
docker run -it --name HA -p 8123:8123 -v config:/config -v backend:/usr/src/app homeassistant/home-assistant:dev
```
