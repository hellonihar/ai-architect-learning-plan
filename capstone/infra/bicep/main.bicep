@description('Capstone infrastructure for AI assistant')
param location string = resourceGroup().location
param appName string
param openAiName string
param searchName string

resource appService 'Microsoft.Web/sites@2023-01-01' = {
  name: appName
  location: location
  kind: 'app'
  properties: {
    serverFarmId: hostingPlan.id
    siteConfig: {
      appSettings: [
        { name: 'OPENAI_ENDPOINT', value: openAi.properties.endpoint }
        { name: 'SEARCH_ENDPOINT', value: search.properties.endpoint }
      ]
    }
  }
}

resource hostingPlan 'Microsoft.Web/serverfarms@2023-01-01' = {
  name: '${appName}-plan'
  location: location
  sku: { name: 'B1', tier: 'Basic' }
}

resource openAi 'Microsoft.CognitiveServices/accounts@2023-10-01-preview' = {
  name: openAiName
  location: location
  kind: 'OpenAI'
  sku: { name: 'S0' }
}

resource search 'Microsoft.Search/searchServices@2023-11-01' = {
  name: searchName
  location: location
  sku: { name: 'standard' }
  properties: { replicaCount: 1, partitionCount: 1 }
}
