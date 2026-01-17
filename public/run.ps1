$uri = "https://raw.githubusercontent.com/Louchatfroff/VORTEX-AUTOUNNATENDED/autunnatended/VORTEX.ps1"
Invoke-RestMethod $uri -UseBasicParsing | Invoke-Expression
