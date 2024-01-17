# IaC

FortiFlex - Ansible and Terraform - Data and Provisioning

## Documentation

- [Ansible Module](https://ansible-galaxy-fortiflexvm-docs.readthedocs.io/en/latest/)
- [Terraform Provider](https://registry.terraform.io/providers/fortinetdev/fortiflexvm/latest/docs)

## Examples

- Ansible
  - fortiflex-data - Retrieves all programs, configurations, and entitlements associated with utilized FortiFlex API credentials.

  > You can specify your username and password in the playbook (not recommended) or the environment variables: FORTIFLEX_ACCESS_USERNAME and FORTIFLEX_ACCESS_PASSWORD.

- Terraform
  - fortiflex-data - Retrieves all programs, configurations, and entitlements associated with utilized FortiFlex API credentials.

  - fortiflex-entitlement - Manage entitlements for the specified program and configuration

  - fortiflex-provision - Manage configuration and entitlements for the specified program.
  