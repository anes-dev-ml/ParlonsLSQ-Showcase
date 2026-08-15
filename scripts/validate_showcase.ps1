param(
    [switch]$Release
)

$ErrorActionPreference = 'Stop'

$arguments = @('scripts/validate_showcase.py')
if ($Release) {
    $arguments += '--release'
}

python @arguments
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
