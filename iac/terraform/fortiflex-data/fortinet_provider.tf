terraform {
  required_providers {
    fortiflexvm = {
      source  = "fortinetdev/fortiflexvm"
      version = "~>2"
    }
  }
}

provider "fortiflexvm" {
}