# Lab: Running tests with nose

These are the source files for the lab **Running tests with node**

Required Python packages are:

- nose
- pinocchio
- coverage

Contents of `setup.cfg` should be:

```ini
[nosetests]
verbosity=2
with-spec=1
spec-color=1
with-coverage=1
cover-erase=1
cover-package=triangle

[coverage:report]
show_missing = True
```
