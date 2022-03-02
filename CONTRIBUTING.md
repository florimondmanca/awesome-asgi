# Contribution Guidelines

All contributions to this list are welcome!

## Adding a project

**Important notes**:

- In order to avoid duplicates, please search [existing pull requests](https://github.com/florimondmanca/awesome-asgi/pulls) before submitting a new one.
- Make sure the project you'd like to add is clearly related to ASGI. General-purpose async projects can be submitted to [awesome-asyncio](https://github.com/timofurrer/awesome-asyncio) instead. Likewise, in general framework-specific projects should be submitted to the corresponding lists, such as [awesome-fastapi](https://github.com/mjhea0/awesome-fastapi).

Edit `README.md`:

- Choose one of the sections available. If no section fits the project, feel free to [add a section](#adding-a-section).
- Add the project to the section (**keep alphabetical order**):
    ```markdown
    - [Project name](https://example.com) - A short description which ends with a period.
    ```
- Check spelling and grammar.
- Remove any trailing white space, and separate all headers, paragraphs, lists and code snippets with an empty line.

Once that's done, you can [submit a PR](https://github.com/florimondmanca/awesome-asgi/compare). :-)

## Adding a section

- Add the section to the table of contents (**keep alphabetical order**):

```markdown
## Contents

- ...
- [My Section Header](#my-section-header)
```

- Add the section header and description in the `README` (**keep alphabetical order**);

```markdown
## My section header

_My section description._
```

## CI

A CI job checks for the order of entries.

To ensure entries are properly sorted locally before pushing a PR, use:

```
make format
```
