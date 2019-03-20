workflow "Push it!" {
  on = "push"
  resolves = ["HA Index"]
}

action "push" {
  uses = "ludeeus/action-push@master"
  env = {
    ACTION_MAIL = "ludeeus@gmail.com"
    ACTION_NAME = "ludeeus"
    ACTION_MESSAGE = "Action commit"
    ACTION_BRANCH = "new-test-branch"
  }
  secrets = ["GITHUB_TOKEN"]
}

action "HA Index" {
  uses = "ludeeus/action-haindex@master"
  secrets = ["GITHUB_TOKEN"]
  needs  = ["push"]
}
