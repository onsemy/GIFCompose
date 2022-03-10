# GIF Composite

A project to insert and export a background image in a transparent GIF.

Input:
> ![](/test.gif) ![](/test.png)

Output:
> ![](/output.gif)

## How to use

```
Usage: main.py [OPTIONS]

Options:
  --output-path TEXT  Output path  [required]
  --gif-path TEXT     GIF path  [required]
  --bg-path TEXT      Background image path  [required]
  --fit-origin        Resize background image from GIF
  --debug             Save to png each frame
  --help              Show this message and exit.
```

> `$ python3 main.py --output-path /path/to/output --gif-path /path/to/gif --bg-path /path/to/background`

## Environments

- Python 3.9.8 above
- Pillow 9.0.1 above
- Click 8.0.4 above

## Requirements for execute

- `$ pip3 install -r requirements.txt`

### Case of using VirtualEnv

- Install VirtualEnv
  - `$ pip3 install virtualenv`
  - `$ virtualenv venv`
  - `$ source ./venv/bin/activate`
- Install dependencies (in VirtualEnv)
  - `(venv)$ pip3 install -r requirements.txt`

## Issue tracking

- [This way](https://github.com/onsemy/GIFComposite/issues)
