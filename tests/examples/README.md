# Example documents

Example documents for testing. Examples are written in a subset of [YAML][yaml] corresponding to JSON with comments.

## Directory structure

```
./tests/examples/${SCHEMA}
├── invalid
│   └── *.yaml
└── valid
    ├── minimal.yaml
    ├── null.yaml
    ├── nullish.yaml
    ├── maximal.yaml
    └── *.yaml
```

Each subdirectory corresponds to a schema in the [OpenADR 3.0.0 specification][spec].

### `${SCHEMA}/valid/` subdirectories

Each schema-subdirectory has its own subdirectory named `valid` that contain only examples that match the schema.
Most `valid/` subdirectories will contain a the following documents:

- `minimal.yaml`: contains the minimum number of fields to be valid
- `null.yaml`: contains all fields that can be `null` as `null`
- `nullish.yaml`: demonstrates values that could be confused with `null`
- `maximal.yaml`: demonstrates all possible fields, often with intentionally odd or nonsensical values
- other documents named like `${name}.yaml`

### `${SCHEMA}/invalid/` subdirectories

Some schema-subdirectories have their own subdirectories named `invalid` that contain realistically invalid values of the schema.

[spec]: ../../spec/1_oadr3.0.0.yaml#/components/schemas
[yaml]: https://yaml.org/
