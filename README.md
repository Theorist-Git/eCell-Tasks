#  eCell-Tasks
* This git repo hosts the static files for the web-dev task of the eCell NSUT.
* Website: https://spectacular-dieffenbachia-bd7694.netlify.app/

## Working
* Code written in flask is first frozen into static files inside the /build directory using Frozen-Flask.
* This git repository acts as the server of static files to netlify.
* Netlify runs a certain script to check for changes to this repo. This way I can constantly develop and integrate the website.
## Overview

* The website is made using flask, a micro-framework for web development in python. 
* I decided to use a dynamic framework to create a static website as with Flask, I could continue to use the following tools:

  * Jinja templates (including template inheritance) for generating HTML code.
  * Development server with auto-reload and debug.
  * Use of blueprints, so if I decide to expand the website further, I could do so in a neat and organized way

* Also, if in the future I decide to make the website dynamic, I would just have to remove Frozen-Flask.

## Usage
Before you can do all this, add this to the top of your app.py and build.py files:
```python
import sys

sys.path.append('path\\to\\your\\website\\folder')
```
Run this command to activate the dev server via Frozen-Flask
```bash
$ python app.py
```

Use the following command to build the static files
```bash
$ python build.py
```

## Author(s)

Contributor names and contact info
* Mayank vats : [Theorist-git](https://github.com/Theorist-Git)
  * Email: dev-theorist.e5xna@simplelogin.com
## License

[MIT](https://choosealicense.com/licenses/mit/)