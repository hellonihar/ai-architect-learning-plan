@description('Azure OpenAI deployment')
param location string = resourceGroup().location
param openAiName string
param deploymentName string
param modelName string = 'gpt-4o'
param modelVersion string = '2024-11-20'
param capacity int = 10

resource openAi 'Microsoft.CognitiveServices/accounts@2023-10-01-preview' = {
  name: openAiName
  location: location
  kind: 'OpenAI'
  sku: {
    name: 'S0'
  }
  properties: {
    customSubDomainName: openAiName
  }
}

resource deployment 'Microsoft.CognitiveServices/accounts/deployments@2023-10-01-preview' = {
  name: '${openAiName}/${deploymentName}'
  parent: openAi
  properties: {
    model: {
      format: 'OpenAI'
      name: modelName
      version: modelVersion
    }
    raiPolicyName: 'Microsoft.Default'
  }
  sku: {
    name: 'Standard'
    capacity: capacity
  }
}

output endpoint string = openAi.properties.endpoint
