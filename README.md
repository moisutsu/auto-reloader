<h1 align="center">Welcome to auto-reloader 👋</h1>
<p>
  <img alt="Version" src="https://badge.fury.io/py/auto-reloader.svg" />
  <a href="https://github.com/moisutsu/auto-reloader/blob/master/LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://twitter.com/moisutsu" target="_blank">
    <img alt="Twitter: moisutsu" src="https://img.shields.io/twitter/follow/moisutsu.svg?style=social" />
  </a>
</p>

> Automatic reloading library for Jupyter

## Install

```sh
pip install auto-reloader
```

## Usage

```python
import module as _module
from auto_reloader import AutoReloader

module = AutoReloader(_module)

instance = module.Class()
```

The module is reloaded when an instance is created with `instance = module.Class()`.

Besides this, the module is reloaded every time you access the `module` attribute.

## Run tests

```sh
poetry run pytest tests
```

## Author

👤 **moisutsu**

* Twitter: [@moisutsu](https://twitter.com/moisutsu)
* Github: [@moisutsu](https://github.com/moisutsu)

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2020 [moisutsu](https://github.com/moisutsu).<br />
This project is [MIT](https://github.com/moisutsu/auto-reloader/blob/master/LICENSE) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
