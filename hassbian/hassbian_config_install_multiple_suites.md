# install multiple suites with `hassbian-config`

```bash
suites='mosquitto samba hue'
for suite in suites; do 
  sudo hassbian-config install $suite --force --accept
done
```
