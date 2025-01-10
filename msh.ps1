Function read {
  param (
  [string]$prompt
  )
  Write-Host "$prompt " -NoNewline
  Microsoft.PowerShell.Utility\Read-Host
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

Function msh {
    cls
    while ($true) {
        $batteries = Get-WmiObject -Class Win32_Battery
        foreach ($battery in $batteries) {
            $charge = $batteries[0].EstimatedChargeRemaining
        }
        $date = Get-Date -Format "dd/MM/yyyy HH:mm"
        try {
            $l = Get-Location
            $lo = $l.ToString()
            $loc = $lo.Replace("$env:USERPROFILE", "~").Replace("\","/")
        } catch {
            $loc = $env:USERPROFILE.ToString().Replace("$env:USERPROFILE", "~").Replace("\","/")
        }
        Write-Host "[" -NoNewline
        Write-Host "$env:USERNAME" -NoNewline -ForegroundColor Red
        Write-Host "@" -NoNewline -ForegroundColor DarkRed
        Write-Host "$env:COMPUTERNAME" -NoNewline -ForegroundColor Blue
        Write-Host "]-[" -NoNewline
        Write-Host "$loc" -NoNewline -ForegroundColor DarkRed
        Write-Host "]"
        Write-Host "$date " -NoNewline -ForegroundColor Magenta
        Write-Host "$" -NoNewline
        $cmd = read ""
        try {
            Invoke-Expression "$cmd"
        } catch {
            Write-Host "ExpressionError: Invalid Expression." -ForegroundColor Red
        }
    }
}