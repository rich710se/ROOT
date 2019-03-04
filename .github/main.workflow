workflow "Issue" {
  on = "issues"
  resolves = [
    "Discord notification",
    "Hello World",
  ]
}

action "Discord notification" {
  uses = "Ilshidur/actions/discord@master"
  secrets = ["DISCORD_WEBHOOK"]
  args = "Action started"
}

action "Hello World" {
  uses = "./actions"
}
