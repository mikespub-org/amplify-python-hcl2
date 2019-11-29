# Terraform Provider Schemas

This directory contains the provider schemas of several Terraform providers as generated via the terraform CLI.

## Using provider schemas in your python scripts

The schemas are split per provider for ease of use. The schema.json file can be loaded as any JSON file.

Each provider schema uses the format described at https://www.terraform.io/docs/commands/providers/schema.html
 
## Current provider schema versions

Terraform v0.12.16
+ provider.aws v2.40.0
+ provider.azurerm v1.36.1
+ provider.google v2.18.1
+ provider.local v1.4.0

## Adding providers or updating the schemas

The provider schemas are generated via the terraform CLI.

If you want to upgrade the schemas to the latest provider versions, run terraform init -upgrade to upgrade the plugins first.

```sh
$ cd test/providers_schemas/<provider>
$ terraform init -upgrade
$ terraform version > version.md
$ terraform providers schema -json > schema.json
```

If you want to add a new provider, create a new directory for it and add it to a provider.tf file.

```sh
$ mkdir test/providers_schemas/<new_provider>
$ cd test/providers_schemas/<new_provider>
$ echo provider "<new_provider>" {} > provider.tf
$ terraform init
$ terraform version > version.md
$ terraform providers schema -json > schema.json
```
