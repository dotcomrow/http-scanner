# Configuration Files

http-scanner is driven by YAML configuration files.

Example:

```yaml
input:
  plugin: http_input
  settings:
    urls:
      - https://example.com

processor:
  plugin: idea_extractor
  settings:
    model: mistral
    chunk_size: 2000

output:
  plugin: console_output
  settings:
    format: pretty
```

| Field | Purpose |
|:------|:--------|
| `input.plugin` | Input plugin to use |
| `processor.plugin` | Processing plugin to apply |
| `output.plugin` | Output plugin to emit results |
