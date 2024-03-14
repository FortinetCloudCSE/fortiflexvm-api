locals {

}

data "fortiflexvm_entitlements_points" "entitlements_points" {
  config_id  = var.config_id
  account_id = var.account_id != null ? var.account_id : null
  start_date = var.start_date != null ? var.start_date : formatdate("YYYY-MM-DD", timeadd(timestamp(), "-720h"))
  end_date   = var.end_date != null ? var.end_date : formatdate("YYYY-MM-DD", timestamp())
}

output "entitlements_points" {
  value = data.fortiflexvm_entitlements_points.entitlements_points
}