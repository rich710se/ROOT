$Logfile = "C:\temp\miner.log"
Function LogWrite
{
   Param ([string]$logstring)
   Add-content $Logfile -value $logstring
}
while ($true) {
	$datetime = (date -Format d)+" "+(date -Format T)
    $SwitchValue = curl https://domain.duckdns.org:8123/api/states/input_boolean.miner?api_password=PASSWORD -UseBasicParsing | select -ExpandProperty RawContentLength
    if ($SwitchValue -Like "206")
        {$Running = Get-Process -Name excavator* | select -ExpandProperty ProcessName | Select-Object -First 1
        if ($Running -notin "excavator") 
            {start "C:\Users\user\AppData\Local\Programs\NiceHash Miner 2\NiceHash Miner 2.exe"
			LogWrite "$datetime - Starting Miner..."}
         else
            {LogWrite "$datetime - Already running..."}
        }
    else 
        {$Running = Get-Process -Name excavator* | select -ExpandProperty ProcessName | Select-Object -First 1
        if ($Running -in "excavator") 
            {Get-Process -Name Nice* | Stop-Process
			Get-Process -Name excavato* | Stop-Process
			LogWrite "$datetime - Stopping Miner..."}
        else
            {LogWrite "$datetime - Already stopped..."}
        }
        
		
    sleep 20
    }
