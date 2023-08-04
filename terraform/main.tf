variable "myvar" {
  type = string
  default = "My name is Berkay"
}
variable "mymap" {
  type = map(string)
  default = {
    mykey = "myvalue"
  }
}
variable "mylist" {
  type = list
  default = [1,2,3]
}
variable "myint" {
  type = number
  default = 1
}
variable "mybool" {
  type = bool
  default = true
}
