# 


#  Tools for figuring out features of LVGL

Copy the app toolscript to ~/.micropython/lib/

```bash
./../lv_micropython/mpy-cross/build/mpy-cross tools/app_tools.py
```

```bash
rsync -avP tools/*.mpy ~/.micropython/lib/
```

## Packages

```python
import mip
mip.install('logging')
```

