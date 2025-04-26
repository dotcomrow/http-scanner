# Plugin Development Guide

## Creating Input Plugins

- Place your input plugin in `src/plugins/inputs/`
- Must define a `fetch(settings)` function.

Example:

```python
def fetch(settings):
    urls = settings.get('urls', [])
    return urls
```

## Creating Processor Plugins

- Place your processor in `src/plugins/processors/`
- Must define a `process(texts, settings)` function.

Example:

```python
def process(texts, settings):
    return [{"original": text, "insights": []} for text in texts]
```

## Creating Output Plugins

- Place your output plugin in `src/plugins/outputs/`
- Must define an `output(processed_data, settings)` function.

Example:

```python
def output(processed_data, settings):
    for record in processed_data:
        print(record)
```

✅ Add your plugin file — no need to touch core code!
