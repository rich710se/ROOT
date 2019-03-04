workflow "Issue" {
  on = "issues"
  resolves = [
    "Discord notification",
  ]
}

action "Discord notification" {
  uses = "Ilshidur/action-discord@master"
  secrets = ["DISCORD_WEBHOOK"]
  args = "Action started"
}
