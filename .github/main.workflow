workflow "Issue" {
  resolves = [
    "Discord notification",
    "Pandoc Document Conversion",
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

action "Pandoc Document Conversion" {
  uses = "maxheld83/pandoc@v0.1.1"
  needs = ["Debug Action"]
}
