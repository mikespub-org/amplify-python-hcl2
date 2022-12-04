terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
    }
  }
}

provider "aws" {}

provider "azurerm" {}

provider "google" {}

provider "local" {}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

provider "kubernetes" {
  config_path    = "~/.kube/config"
  config_context = "minikube"
}
