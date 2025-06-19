resource storage 'Microsoft.Storage/storageAccounts@2022-09-01' = {
  name: 'datastorage${uniqueString(resourceGroup().id)}'
  location: resourceGroup().location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    accessTier: 'Hot'
  }
}

resource adf 'Microsoft.DataFactory/factories@2018-06-01' = {
  name: 'datafactory${uniqueString(resourceGroup().id)}'
  location: resourceGroup().location
  properties: {}
}

