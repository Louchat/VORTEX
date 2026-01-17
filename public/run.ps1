$uri = "https://raw.githubusercontent.com/Louchatfroff/VORTEX-AUTOUNNATENDED/main/install.bat"
Invoke-RestMethod $uri -UseBasicParsing | Invoke-Expression
