<#
.intro
This is neofetch for
windows basically
#>

Function neofetch{
    param (
        [string]$artcolour="Cyan"
    )

$art = @(
"llllllllll  llllllllll",
"llllllllll  llllllllll",
"llllllllll  llllllllll",
"llllllllll  llllllllll",
"                      ",
"llllllllll  llllllllll",
"llllllllll  llllllllll",
"llllllllll  llllllllll",
"llllllllll  llllllllll"
)

$art = $art -join "`n"
$date = Get-Date -Format "dddd dd/MM/yyyy HH:mm K"

Write-Host "$art`n" -ForegroundColor $artcolour
Write-Host "== Specifications ==`n" -ForegroundColor White -BackgroundColor Blue
Write-Host "Current date: " -NoNewline -ForegroundColor Magenta
Write-Host "$date"
Write-Host "PowerShell Version: " -NoNewline -ForegroundColor Green
$PSVersionTable.PSVersion.Major, $PSVersionTable.PSVersion.Minor -join "."
Write-Host "Execution Policy: " -NoNewline -ForegroundColor Red
Get-ExecutionPolicy
Write-Host "Drives: " -NoNewline -ForegroundColor Blue
Get-PSDrive
Write-Host "Processor: " -NoNewline -ForegroundColor Cyan
Get-WmiObject Win32_Processor
Write-Host "Top-Processes: " -NoNewline -ForegroundColor Yellow
$processes = Get-Process | Sort-Object -Property CPU -Descending | Select-Object -First 3

$result = @()

foreach ($process in $processes) {
    $obj = New-Object -TypeName PSObject
    $obj | Add-Member -MemberType NoteProperty -Name "Name" -Value $process.Name
    $obj | Add-Member -MemberType NoteProperty -Name "CPU" -Value $process.CPU
    $obj | Add-Member -MemberType NoteProperty -Name "Memory" -Value $process.WorkingSet
    $result += $obj
  }
$result

Write-Host "`nScript made by Elis Staaf" -NoNewline -ForegroundColor White -BackgroundColor Blue
}
