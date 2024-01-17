data "fortiflexvm_programs_list" "programs_list" {}

output "programs_list" {
  value = var.enable_output ? data.fortiflexvm_programs_list.programs_list : null
}