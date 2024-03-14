terraform {
  required_providers {
    fortiflexvm = {
      source  = "fortinetdev/fortiflexvm"
      version = "~>2.3.0"
    }
  }
}

provider "fortiflexvm" {
}