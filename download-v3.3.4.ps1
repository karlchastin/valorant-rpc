# Script pour telecharger la version v3.3.4 depuis https://github.com/krvntzkl/valorant-rpc
# Executez ce script dans PowerShell depuis la racine du projet si le telechargement auto a echoue.

$ErrorActionPreference = 'Stop'
$url = "https://github.com/krvntzkl/valorant-rpc/archive/refs/tags/v3.3.4.zip"
$zipPath = Join-Path $PSScriptRoot "v3.3.4.zip"
$extractTo = Join-Path $PSScriptRoot "v3.3.4"

Write-Host "Telechargement de v3.3.4 depuis GitHub..."
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
Invoke-WebRequest -Uri $url -OutFile $zipPath -UseBasicParsing

Write-Host "Extraction dans $extractTo..."
if (Test-Path $extractTo) { Remove-Item $extractTo -Recurse -Force }
Expand-Archive -Path $zipPath -DestinationPath $PSScriptRoot -Force
$extractedFolder = Get-ChildItem $PSScriptRoot -Directory | Where-Object { $_.Name -like "valorant-rpc-*" } | Select-Object -First 1
if ($extractedFolder) {
    New-Item -ItemType Directory -Path $extractTo -Force | Out-Null
    Get-ChildItem $extractedFolder.FullName | Move-Item -Destination $extractTo -Force
    Remove-Item $extractedFolder.FullName -Force
}
Remove-Item $zipPath -Force
Write-Host "Termine. Contenu disponible dans le dossier v3.3.4"
