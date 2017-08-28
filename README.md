# `acmatfsu.org`
Association for Computing Machinery at Florida State University chapter homepage.


## `src` explained

#### `locals.js`

Constant data passed as variables to `.pug` templates. May not update on watch.

### Folder structure

Different views on the site are modularized into subfolders containing view
specific formatting, content, styles, and code. Each type of file is flattened
during the build stage such that all `.pug` files are built into `.html` and
stored in the default directory. All `.sass` files are build into `.css` and
moved to the `/css` folder, and so on.

```

src
├── locals.js       // universal variables
├── default.sass    // default styles
├── template.pug    // default page template
│
├── index
│   ├── index.pug
│   ├── index.sass
│   └── index.js
│
├── officers        (just an example view)
│   ├── officers.pug
│   ├── officers.sass
│   └── officers.js
...

```
