data "fortiflexvm_configs_list" "configs_list" {

  for_each = local.programs_map

  program_serial_number = each.value.serial_number
}

output "configs_list" {
  value = var.enable_output ? data.fortiflexvm_configs_list.configs_list : null
}