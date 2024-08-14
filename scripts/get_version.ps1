Get-Content -Path ".\.lip\metadata\github.com%2FLiteLDev%2Fbds.json" |   
    Select-String -Pattern "bdsdown.exe -y" |   
    ForEach-Object {  
        if ($_ -match 'windows/([^"]+)') {  
            $_.Matches[0].Groups[1].Value.TrimEnd('/')  
        }  
    }
