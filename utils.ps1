<# 
.intro
utils.py, Functions i felt were to important to lose. 
#>

# Variables

$location = Get-Location
$lastlocation = Pop-Location
$getverb = Get-Verb | Sort-Object -Property Verb
$ComputerName = $env:COMPUTERNAME
$cmds = Get-Command

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

Function Get-Version {    
    $PSVersionTable.PSVersion
}

Function printf { 
  param (
    [string]$Text
)          
  Write-Host "$Text"
}

Function Check-DiskSpace {
  param (
      [string]$DriveLetter = "C",
      [int]$ThresholdGB = 10
  )
  $drive = Get-PSDrive -Name $DriveLetter
  $freeSpaceGB = [math]::Round($drive.Free / 1GB, 2)
  if ($freeSpaceGB -lt $ThresholdGB) {
      Write-Output "Warning: Free space on drive $DriveLetter is below $ThresholdGB GB. Current free space: $freeSpaceGB GB."
  } else {
      Write-Output "Drive $DriveLetter has sufficient free space: $freeSpaceGB GB."
  }
}

Function Backup-Files {
  param (
      [string]$SourceDirectory,
      [string]$DestinationDirectory
  )
  if (-Not (Test-Path $SourceDirectory)) {
      Write-Output "Source directory does not exist."
      return
  }
  if (-Not (Test-Path $DestinationDirectory)) {
      New-Item -ItemType Directory -Path $DestinationDirectory
  }
  Copy-Item -Path "$SourceDirectory\*" -Destination $DestinationDirectory -Recurse -Force
  Write-Output "Backup completed from $SourceDirectory to $DestinationDirectory."
}

Function Execution-Policy {
  param (
    [Parameter(Mandatory)]
    [string]$scope, $policy
  )
  Set-ExecutionPolicy -scope $scope -ExecutionPolicy $policy
}

Function cd {
  param (
    [string]$dir
  )
  Set-Location "$dir"
}

Function ls {
  param (
    [bool]$force=$false
  )
  if ($force -eq $true) {
    Get-ChildItem -Force 
  }
  else {
    Get-ChildItem 
  }
}

Function Get-TopProcesses {
  Param(
      [int]$count = 10
  )

  $processes = Get-Process | Sort-Object -Property CPU -Descending | Select-Object -First $count

  $result = @()

  foreach ($process in $processes) {
      $obj = New-Object -TypeName PSObject
      $obj | Add-Member -MemberType NoteProperty -Name "Name" -Value $process.Name
      $obj | Add-Member -MemberType NoteProperty -Name "CPU" -Value $process.CPU
      $obj | Add-Member -MemberType NoteProperty -Name "Memory" -Value $process.WorkingSet
      $result += $obj
  }

  return $result
}

Function Get-ServiceStatus {
    param (
        [string]$ServiceName
    )
 
    $service = Get-Service -Name $ServiceName -ErrorAction SilentlyContinue
 
    if ($Service.Status -eq "Running") {
        return "Service is running"
    } else {
        return "Service is not running"
    }
}

Function cat {
  Param(
      [Parameter(Mandatory=$true)]
      [string]$path
  )
  Get-Content $path
}

Function mkfile {
  param (
    [Parameter(Mandatory)]
    $path
  )
  if (-not $path -eq "") {
    New-Item $path
  }
  else {
    Write-Host "Filename cannot be empty."
  }
}

Function mkdir {
  param (
    [Parameter(Mandatory)]
    $path
  )
  if (-not $path -eq "") {
    New-Item -ItemType Directory -Path $path
  }
  else {
    Write-Host "Directory name cannot be empty."
  }
} 

Function openfile {
  param (
    [Parameter(Mandatory)]
    $path
  )
  if (-not $path -eq "") {
    Invoke-Item -Path $path
  }
  else {
    Write-Host "Filename cannot be empty."
  }
} 

Function testfile {
  param (
    [Parameter(Mandatory)]
    $path
  )
  if (-not $path -eq "") {
    Invoke-Item -Path -WhatIf $path
  }
  else {
    Write-Host "Filename cannot be empty."
  }
} 
