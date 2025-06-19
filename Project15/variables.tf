variable "aws_region" {
  default = "ap-south-1"
}

variable "ami_id" {
  description = "AMI ID for the EC2 instance"
}

variable "instance_type" {
  default     = "t2.micro"
  description = "Type of EC2 instance"
}

variable "key_name" {
  description = "SSH Key Pair Name"
}
