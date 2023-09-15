#####    Craft demo  #####
## How to execute the lookup script Locally normaly and as cli
1. Add an alias in ~/.bashrc file as alias lookup='python3 /path/to/countrylookup.py'
2. source ~/.bashrc
3. lookup --countryCode AU 
4. lookup --countryCode AU DE
5. python3 countrylookup.py --countryCode AU
6. python3 countrylookup.py --countryCode AU, CA, DE


##### Bonus #####
## How to Access this using K8s in Local

1. setup a minikube in the Local env
2. create the Docker image from the Dockerfile
3. create the k8s service using < kubectl apply -f service.yaml> command
4. Run the pod using kubectl command < kubectl run country-lookup --image=country-lookup:latest --image-pull-policy=Never --port=5000 >
5. kubectl port-forward pods/<podname> 8080:5000
6. Access the URL using  Curl method and pass the Country Code "curl -X POST -H 'Content-Type: application/json' -d '{"country_code": "US"}' http://localhost:5000/convert"
7. curl  http://127.0.0.1/health
8. curl  http://127.0.0.1/diag


#### Monitoring Setup for monitoring Pod  ####

I have written a K8s cronjob configuration that will check the status of the pod health every 1 minute.

## How to create the Cronjob

kubectl apply -f monitor.yaml