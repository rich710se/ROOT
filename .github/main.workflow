workflow "Push it!" {
  on = "push"
  resolves = ["push"]
}

action "push" {
  uses = "ludeeus/action-push@master"
  env = {
    ACTION_MAIL = "ludeeus@gmail.com"
    ACTION_NAME = "ludeeus"
    ACTION_MESSAGE = "Action commit"
    ACTION_BRANCH = "master"
  }
  secrets = ["GITHUB_TOKEN"]
  needs = ["HA Index"]
}

action "HA Index" {
  uses = "ludeeus/action-haindex@master"
  secrets = ["GITHUB_TOKEN"]
}
