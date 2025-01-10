Function Format-Prompt {
  <#

  .Intro
  Formatter function for user inputs.

  .HowToUse
  To use, please pass a string into the $output param,
  then use the ToString() function to accquire the
  output, then use it for your own code.

  .Example
  $formatter = Format-Prompt -prompt "Enter name: "
  $name = $formatter.ToString()

  .Outro
  Yeah, so, uhh, please enjoy! :)

  #>
  param (
    [Parameter(Mandatory)]
    [string]$prompt
  )
  PROCESS {
    $output = Read-Host "$prompt"
    return $output
  }
}

Function Format-List {
  <#

  .Intro
  List strings in a format.

  .HowToUse
  To use, please pass a string into the $s params.

  .Example
  $formatter = Format-List "Carl" "Bob" "Roger" "David" "Marcus" "Fredric"

  .Outro
  Yeah, so, uhh, please enjoy! :)

  #>
  param (
    [Parameter(Mandatory)]
    [string[]]$array
    )
    $l = 0
    $c = 0
    foreach ($i in $array) {
      $c += 1
      $j = $array[$l]
      Write-Host "$c | $j"
      $l += 1
    }
}

Function Format-Header {
  <#

  .Intro
  Formatting headers!.

  .HowToUse
  To use, please pass a string into the $header param.

  .Example
  $header = Format-Header "A guide to the PowerShell module: formatter"

  .Outro
  Yeah, so, uhh, please enjoy! :)

  #>
  param (
  [Parameter(Mandatory)]
  [string]$header
  )
  Write-Host " $header"
  $separator = @()
  $splitheader = $header -Split ""
  foreach ($i in $splitheader) {
    $separator += "-"
  }
  $border = -Join $separator
  Write-Host "$border"
}

Function Format-Paragraph {
  <#

  .Intro
  Formatting paragraphs!.

  .HowToUse
  To use, please pass a string into the $line params.

  .Example
  $paragraph = "This is an essay." "Pretty cool." "Yeah."

  .Outro
  Yeah, so, uhh, please enjoy! :)

  #>
  param (
  [Parameter(Mandatory)]
  [string]$line1,
  $line2, $line3
  ) 
  Write-Host "$line1`n$line2`n$line3"
}

Function Format-Date {
  <#

  .Intro
  Date formatting!.

  .HowToUse
  To use, please pass a string into the $format params,
  then use the ToString() function to accquire the
  output, then use it for your own code.

  .Example
  $date = Format-Date "MM/dd/yyyy HH:mm:ss"
  $output = $date.ToString()

  .Outro
  Yeah, so, uhh, please enjoy! :)

  #>
  param (
    [string]$format="dd/MM/yyyy HH:mm:ss"
  )
  $date = get-date -format $format
  return $date
}