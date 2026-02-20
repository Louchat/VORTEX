$batUrl = "https://raw.githubusercontent.com/Louchatfroff/VORTEX-AUTOUNNATENDED/main/install.bat"
$localBat = "$env:TEMP\install.bat"
Invoke-WebRequest -Uri $batUrl -OutFile $localBat
Start-Process -FilePath $localBat -Wait
