

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