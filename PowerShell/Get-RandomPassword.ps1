<#
.SYNOPSIS
   To Generate a random password
.DESCRIPTION
   This script with generate a random password of given length, 
   without any special characters, expect punctuation. 
   Based on the ASCII character set, the below characters are used:
   Alphabets between this ranges: (65 to 90) and (97 to 122)
   digits between (48 and  57)
   puncutation character
.PARAMETER <paramName>
   Get-RandomPassword <length>
.EXAMPLE
   Get-RandomPassword 15
#>

Param(
[int] $length
)

Function Get-RandomPassword ($length = 15)
{    
    # Restricting the characters in the generating password
    $alphabets = 65..90 + 97..122
    $digits = 48..57
    $punc = 46..46
    $password = Get-Random -count $length -input ($punc + $digits + $alphabets) |`
      ForEach-Object -begin { $aa = $null } -process {$aa += [char]$_} -end {$aa}

    return $password
}

Get-RandomPassword $length