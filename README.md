# Example FastAPI Application

This repository is an example application that uses what I consider good
practices for developer experience, testing, and deployment.


## Development

### Prerequisites
if you will develop the repo, a prerequisite is running `pre-commit`.
`pre-commit` is already included as a dependency, so if all packages are
installed, you just need to run at the command line

```commandline
pre-commit install
```

to run the configured pre-commit hooks before a committing.

The hooks that are run are
- built in hooks to remove extra trailing white space, and an extra line
  return as needed at the end of a file
- `isort` sorts the imports
- `black` is an opinionated code formatter that will automatically edit your
  files. includes a default width of 88 characters
- `flake8` is also a code formatter, that checks for errors, and complexity,
  asking you to fix the errors.

You'll need to have all hooks pass before the commit can happen. Pre-commit
usually runs only on files added in the commit.
