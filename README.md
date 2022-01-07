# RecipesMountain

Requiremtnes:
* Docker
* Docker-Compose
* Poetry
* npm

## Building 

To build docker images run:
```
docker-compose build
```
This will build docker images for Frontend as well as Backend

### Building Backend:
Backend doesn't have to be build it can be run right away using in `services/backend`
```
Poetry run
```

### Building frontend
Fronend can be build by running
```
npm run build
```
in `services/frontend`

## Deployment

Starting application locally
```
docker-compose up -d
```

Stoping 
```
docker-compose down 
```
In order to remove volumes add `-v` after down 


## Deployment to GKE

Create cluster on GKE, add trigger to Cloud Build and create repository in GCP, change in `cloudbuild.yaml` you region, cluster name and repository. When trigger fires deployment will happen automaticly 


