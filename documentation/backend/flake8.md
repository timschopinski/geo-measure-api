To run flake8

```nashorn js
docker compose run --rm django flake8 --config=./pyproject.toml
```

Modify pyproject.toml in case some errors have to be skipped or use # noqa in code to skip validation in a specific line

[See documentation](https://flake8.pycqa.org/en/latest/)
