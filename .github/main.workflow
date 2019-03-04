workflow "Issue" {
  resolves = [
    "Discord notification",
    "Debug Action",
  ]
  on = "push"
}

action "Discord notification" {
  uses = "Ilshidur/action-discord@master"
  secrets = ["DISCORD_WEBHOOK"]
  args = "Action started"
}

action "Debug Action" {
  uses = "hmarr/debug-action@v1.0.0"
}
