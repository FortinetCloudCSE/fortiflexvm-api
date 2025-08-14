variable "program_serial_number" {
  description = "FortiFlex Program Serial Number"
  type        = string
  default     = null
}

variable "account_id" {
  description = "FortiFlex Account ID"
  type        = string
  default     = null
}

variable "config_id" {
  description = "FortiFlex Configuration ID"
  type        = string
}

variable "start_date" {
  description = "Start date for the report"
  type        = string
  default     = null
}

variable "end_date" {
  description = "End date for the report"
  type        = string
  default     = null
}

variable "enable_output" {
  description = "Enable/Disable output"
  default     = true
}
