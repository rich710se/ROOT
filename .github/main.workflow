workflow "Push it!" {
  on = "push"
  resolves = ["push"]
}

action "push" {
  uses = "ludeeus/action-push@master"
  env = {
    ACTION_MAIL = "ludeeus@gmail.com"
    ACTION_NAME = "ludeeus"
    ACTION_BRANCH = "master"
    ACTION_MESSAGE = "Action commit"
  }
  secrets = ["GITHUB_TOKEN"]
}
