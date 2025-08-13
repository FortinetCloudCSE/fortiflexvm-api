data "fortiflexvm_configs_list" "configs_list" {
  program_serial_number = local.program_serial_number
}

output "configs_list" {

  value = var.enable_output ? data.fortiflexvm_configs_list.configs_list : null
}
