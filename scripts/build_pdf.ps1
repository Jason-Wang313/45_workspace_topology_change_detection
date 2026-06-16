$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Root = Split-Path -Parent $ScriptDir
$PaperDir = Join-Path $Root "paper"
$DataDir = Join-Path $Root "data"
$DownloadsPdf = "C:\Users\wangz\Downloads\45.pdf"
$LocalPdf = Join-Path $PaperDir "main.pdf"
$BuildStatus = Join-Path $DataDir "build_status.json"

New-Item -ItemType Directory -Force -Path $DataDir | Out-Null

Push-Location $PaperDir
try {
    foreach ($pass in 1..3) {
        pdflatex -interaction=nonstopmode -halt-on-error main.tex | Out-Null
        if ($LASTEXITCODE -ne 0) {
            throw "pdflatex failed on pass $pass"
        }
    }

    if (-not (Test-Path -LiteralPath $LocalPdf)) {
        throw "Expected PDF was not produced: $LocalPdf"
    }

    Copy-Item -LiteralPath $LocalPdf -Destination $DownloadsPdf -Force
    $Hash = (Get-FileHash -LiteralPath $DownloadsPdf -Algorithm SHA256).Hash
    Remove-Item -LiteralPath $LocalPdf -Force

    $status = [ordered]@{
        paper = 45
        status = "final_v3_full_scale"
        canonical_pdf = $DownloadsPdf
        canonical_sha256 = $Hash
        local_pdf_removed = -not (Test-Path -LiteralPath $LocalPdf)
        built_at = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss zzz")
    }

    $status | ConvertTo-Json | Set-Content -Path $BuildStatus -Encoding UTF8
}
finally {
    Pop-Location
}
