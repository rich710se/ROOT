$outfile = 'E:\GDRIVE\BACKUP\installedsoftware.txt'
Remove-Item $outfile
Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* |  Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Format-Table -AutoSize | Out-File $outfile
