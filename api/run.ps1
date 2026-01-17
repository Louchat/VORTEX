Write-Output "Content-Type: text/plain`n"
$uri = "https://raw.githubusercontent.com/Louchatfroff/VORTEX-AUTOUNNATENDED/refs/heads/autunnatended/install.bat"
Invoke-RestMethod -Uri $uri -UseBasicParsing | Invoke-Expression
