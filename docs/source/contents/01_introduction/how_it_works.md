How it works
------------

By exploiting the
[uniCMS handlers](https://unicms.readthedocs.io/en/latest/contents/developer.html#handlers)
mechanism, this app generates a series of dynamic webpaths which,
using the API resources assigned to each class,
render the obtained results through a specific template.

Each template integrates a [Vue.js](https://vuejs.org/) component that
takes care of invoking the passed resource and retrieving the data.
