workflow "Issue" {
  on = "issues"
  resolves = ["docker://ludeeus/tasks"]
}

action "docker://ludeeus/tasks" {
  uses = "docker://ludeeus/tasks"
}
