# AppProps

AppsProps is a utility library used to retrieve configuration settings from a configuration YAML file.

### Usage
The class follows a [single pattern](https://python-patterns.guide/gang-of-four/singleton/) so it needs to read the config file once. To initialize, import and call `AppProps('', '<your-config-file-path>')` with the default of `configuration.yml` at the same level as the call. Subsequent calls need only to specify a period-delimited configuration path (see tests for examples.)
