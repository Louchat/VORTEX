Write-Output "Content-Type: text/plain`n"
$uri = "https://raw.githubusercontent.com/Louchatfroff/VORTEX-AUTOUNNATENDED/autunnatended/VORTEX.ps1"
Invoke-RestMethod -Uri $uri -UseBasicParsing | Invoke-Expression
