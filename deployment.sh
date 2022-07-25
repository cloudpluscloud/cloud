az deployment group create \
  --name storagedeployment \
  --resource-group C-Stack-Group \
  --template-file ./personalizedeploy.json \
  --parameters ./parameters.json