Function cat {
  Param(
      [Parameter(Mandatory=$true)]
      [string]$path
  )
  Get-Content $path
}

Function touch {
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

Function Read-Host {
    param (
    [string]$prompt
    )
    Write-Host "$prompt " -NoNewline
    Microsoft.PowerShell.Utility\Read-Host
}

Function Eval-Expr {
    param (
        $cmd
    )

    if ($cmd[0] -eq "touch") {
        touch $cmd[1]
    } if ($cmd[0] -eq "cat") {
        cat $cmd[1]
    } if ($cmd[0] -eq "mkdir") {
        mkdir $cmd[1]
    } if ($cmd[0] -eq "touch") {
        touch $cmd[1]
    } if ($cmd[0] -eq "cd") {
        cd $cmd[1]
    } if ($cmd[0] -eq "ls") {
        ls $cmd[1]
    } if ($cmd[1] -eq ">>") {
        $cmd[0] >> $cmd[2]
    } if ($cmd[0] -eq "#") {

    } else {
        Write-Host "SyntaxError: Invalid Syntax." -ForegroundColor Red
    }
}

$art = @(
"              .__     ",
"  ____   _____|  |__  ",
"_/ ___\ /  ___/  |  \ ",
"\  \___ \___ \|   Y  \",
" \___  >____  >___|  /",
"     \/     \/     \/ "
)
Write-Host "$($art -join "`n")" -ForegroundColor Red
Write-Host "`nCShell or CSH is an interactive, open-source, and free`nshell written in powershell. " -NoNewline
Write-Host "Type `"end`" to exit and `"help`" for help. `n`n" -NoNewLine

for (;;) {
        $location = Get-Location
        $location = $location.ToString().Replace("$env:USERPROFILE", "~").Replace("\","/")
        Write-Host "[" -NoNewline
        Write-Host "$env:USERNAME" -NoNewline -ForegroundColor Red
        Write-Host "@" -NoNewline -ForegroundColor DarkRed
        Write-Host "$env:COMPUTERNAME" -NoNewline -ForegroundColor Blue
        Write-Host "]-[" -NoNewline
        Write-Host "$($location)" -NoNewline -ForegroundColor DarkRed
        Write-Host "]"
        Write-Host "$" -NoNewline
        $cmd = Read-Host ""
        $cmd = $cmd -split " "
        Eval-Expr $cmd
}