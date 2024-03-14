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
