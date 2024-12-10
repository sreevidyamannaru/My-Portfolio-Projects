
provider "aws" {
  region = var.region
}

resource "aws_s3_bucket" "example" {
  bucket = var.bucket_name
  acl    = "private"

  tags = {
    Name        = "My-Terraform-Bucket"
    Environment = "Dev"
  }
}
            