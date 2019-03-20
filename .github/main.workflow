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
    ACTION_BRANCH = "test-branch"
  }
  secrets = ["GITHUB_TOKEN"]
  needs = ["Create file"]
}

action "Create file" {
  uses = "finnp/create-file-action@master"
  env = {
    FILE_NAME = "example.md"
    FILE_DATA = "#Example file\nThis is an example"
  }
}
