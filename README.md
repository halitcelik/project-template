# Resources


# Local project setup
```
git clone git@github.com:cruncher/{{project_name}}.git
cd {{project_name}}
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip wheel
pip install -r requirements.txt
cd {{project_name}}
git submodule update --init
createdb {{project_name}}
python manage.py migrate
cp {{project_name}}/settings/local.py-template {{project_name}}/settings/local.py
python manage.py runserver
```

# {{project_name}}

`https://{{project_name}}.ch/` – prod

`https://{{project_name}}.cruncher.ch/` – staging


## Building front-end resources

From the project directory `{{project_name}}/`...

`git submodule update --init`

Installs the node dependencies listed in `package.json`.

`make modules`

Builds CSS and JS assets from `static/module.css` to `static/build/module.css` and `static/module.js` to `static/build/module.js`.

`make docs`

Builds documentation – a component styleguide – from `source/index.template.html`
to `static/docs/index.html`.

## Writing front-end documentation

Comments in both CSS and JS files are compiled as documentation. Documentation
comments should follow the pattern:

```css
/**
.component-class

```` ```html
<div class="component-class">Example HTML</div>
```` ```

Text description in markdown.
**/
```

The same pattern may be followed in JS:

```js
/**
functionName(param1, param2)

```` ```js
<div class="component-class">Example HTML</div>
```` ```

Text description in markdown.
**/
```

You must add files containing documentation comments to the relevant section
of `source/index.template.html`. It which uses [Literal](https://stephen.band/literal)
templates to generate html.
