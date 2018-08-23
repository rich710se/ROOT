$path = "C:\users\user\downloads\"
Get-ChildItem -Path $path -Recurse | Foreach-object {Remove-item -Recurse -path $_.FullName }
