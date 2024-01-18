# IaC

FortiFlex - Ansible and Terraform - Data and Provisioning

## Documentation

- [Ansible Module](https://ansible-galaxy-fortiflexvm-docs.readthedocs.io/en/latest/)
- [Terraform Provider](https://registry.terraform.io/providers/fortinetdev/fortiflexvm/latest/docs)

## Examples

- Ansible
  - fortiflex-data - Retrieves all programs, configurations, and entitlements associated with utilized FortiFlex API credentials.

- Terraform
  - fortiflex-data - Retrieves all programs, configurations, and entitlements associated with utilized FortiFlex API credentials.

  - fortiflex-entitlement - Manage entitlements for the specified program and configuration

  - fortiflex-provision - Manage configuration and entitlements for the specified program.

## Authentication

FortiFlex API username and password can be specified in an Ansible Playbooks and the Terraform provider definition. Neither of these methods are recommended.

The recommended way to authenticate is by using environment variables:

- FORTIFLEX_ACCESS_USERNAME
- FORTIFLEX_ACCESS_PASSWORD
