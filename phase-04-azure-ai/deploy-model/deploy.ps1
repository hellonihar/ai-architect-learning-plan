param(
    [Parameter(Mandatory = $true)]
    [string]$ResourceGroupName,

    [Parameter(Mandatory = $true)]
    [string]$Location,

    [Parameter(Mandatory = $true)]
    [string]$OpenAiName,

    [Parameter(Mandatory = $false)]
    [string]$DeploymentName = "gpt-4o-deployment",

    [Parameter(Mandatory = $false)]
    [string]$ModelName = "gpt-4o",

    [Parameter(Mandatory = $false)]
    [string]$ModelVersion = "2024-11-20",

    [Parameter(Mandatory = $false)]
    [int]$Capacity = 10
)

# Ensure logged in
az account show --output none
if (-not $?) {
    az login
}

# Create resource group
az group create --name $ResourceGroupName --location $Location

# Deploy bicep
az deployment group create `
    --resource-group $ResourceGroupName `
    --template-file "./bicep/main.bicep" `
    --parameters "./bicep/parameters.json" `
    --parameters openAiName=$OpenAiName `
    --parameters deploymentName=$DeploymentName `
    --parameters modelName=$ModelName `
    --parameters modelVersion=$ModelVersion `
    --parameters capacity=$Capacity

Write-Host "Deployment complete. Endpoint and keys can be retrieved from the Azure portal." -ForegroundColor Green
