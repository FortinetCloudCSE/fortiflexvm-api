data "fortiflexvm_entitlements_list" "entitlements_list" {

  for_each = local.configs_map

  config_id = each.value.id
}

output "entitlements_list" {
  value = var.enable_output ? data.fortiflexvm_entitlements_list.entitlements_list : null
}
