# Flood-Hacked
*...80 dams opened, 325 dead, Kerala needs us*

## Introduction
A web app which provides an optimal solution to distribute food across all the relief shelters in a city, given limited resources including limited number of helicopters, drones, fuel, food supply and most importantly, time. 

## Working and Implementation
<ul>
<li>Our project requires a certain preprocessing, that is, a survey would have to be conducted where in drones will fly over the concerned territory and record locations of all the shelter homes. These locations will be inputted to our application and using the google map api, we can easily generate the geocodes of all the shelter homes.
<li>Apart from these locations as an input, the second input we would be needing is the number of helicopters and drones available for the operation which will be constrained by the government's budget.
<li>Having taken the necessary inputs, the algorithm to decide where should each helicopter release its drones and to which places should each drone drop supplies is as follows:
<ol>
  <li> Let the number of helicopters available be k. So, we divide the shelter homes into k clusters. Each cluster will have one helicopter each releasing drones for the distribution of supplies within that cluster.
  <li> To divide the homes into clusters, k means clustering is used, which uses geocode, water level and population density of these locations as the features.
  <li> Once we have the clusters, we compute the centroid of each cluster where helicopter will be sent.
  <li> Now we have to divide the available drones among these clusters, which is done in poroportion to the number of shelter homes in a cluster. The more the number of shelter homes a cluster has, higher number of drones are assigned to it.
  <li> To further define the group of homes for each drone, k means algorithm is used again. Suppose for a cluster i, we have a<sub>i</sub> drones. So we perform k means with k equal to a<sub>i</sub>.
    <li> Thus we have the geocodes of the centroids where each helicopter will be releasing the drones and also the locations where each drone will be distributing supplies.
</ol>
</ul>

## Installation Requirements

```
Framework : Django, Version : 1.11.8
Language : Python, Version : 3.6.3

To run it, you need to install some packages and libraries as follows:
Bootstrap 3
numpy
sklearn
bcrypt
django[argon]

To install these, write this on the command line terminal:
"pip install package-name"
```

## To run

```
Clone this repo
cd into this repo
Enter the command: "python manage.py runserver"
Copy the url and paste it in your favourite browser window.
```

## See for yourself:
![screenshot 193](https://user-images.githubusercontent.com/31369977/44306839-896f1780-a3b4-11e8-9d02-c1a27f0ffe13.png)
![screenshot 197](https://user-images.githubusercontent.com/31369977/44306841-8f64f880-a3b4-11e8-8723-f448d316cb94.png)
![screenshot 198](https://user-images.githubusercontent.com/31369977/44306842-92f87f80-a3b4-11e8-97ca-fed333b39905.png)
![screenshot 199](https://user-images.githubusercontent.com/31369977/44306844-95f37000-a3b4-11e8-91f0-a4cbb073a05d.png)
![screenshot 200](https://user-images.githubusercontent.com/31369977/44306846-97bd3380-a3b4-11e8-8fbe-1d4e67af1e34.png)


This project was made collectively by [Mansi Breja](https://github.com/MansiBreja), [Anjali Agarwal](https://github.com/aganjali10), [Aastha Agrawal](https://github.com/aastha980) and [Anmol Jain](https://github.com/anmol-1602) as a part of the HackIIITD, Esya'18. 
