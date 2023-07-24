# The Datenzwerg

![Datenzwerg logo](assets/images/logo.png){: style="width:33%;float:right" :}

## What is the Datenzwerg?

The Datenzwerg is a garden gnome with a mission: To collect environmental data and make it publicly available. 

It was originally developed for the [Chaos Communication Camp 2023](https://events.ccc.de/camp/2023/infos/) where we ([@romses](https://chaos.social/@romses) and [@foosel](https://chaos.social/@foosel)) plan to deploy a small army of 10 Datenzwerge across the camp grounds: Happy, Doc, Grumpy, Dopey, Bashful, Sleepy, Sneezy, Nerdy, Kinky and Hefty[^1].

The Datenzwerg consists of a 3D printed gnome body, a custom PCB with an ESP8266 D1 Mini microcontroller board, a BME280, UV and sound sensor and an 18650 battery. It's powered by [ESPHome](https://esphome.io/) and sends its data to an [InfluxDB](https://www.influxdata.com/) instance. The firmware currently logs temperature, relative and absolute humidity, air pressure, dew point and UV index. The goal is to also have it log sound pressure by the time of the camp.

We asked ChatGPT to describe the Datenzwerg for us[^2] and this is what it came up with:

> Welcome to the world of the Datenzwerg, an enchanting garden gnome with a technological twist! 
> This delightful little creature may look like your average garden decoration, 
> but it harbors a secret mission that is as intriguing as it is important. 
> The Datenzwerg is on a quest to collect environmental data and make it publicly available for the benefit of all.
> 
> [...]
> 
> By leveraging its unique vantage point in gardens and outdoor spaces, 
> the Datenzwerg provides an unparalleled perspective on the environment around us.
> 
> All the data collected by these pint-sized environmental guardians is made freely 
> available to the public through an intuitive online platform. 
> 
> [...]
> 
> At the upcoming Chaos Communication Camp, we are excited to introduce the Data Gnome to a 
> wider audience of tech enthusiasts, hackers, and environmental advocates. 
> This extraordinary convergence of nature and technology showcases the potential for 
> citizen-driven environmental monitoring. 

## A short history of the Datenzwerg

2023-06-11
: The idea of the Datenzwerg is born at the final day of  [GPN21](https://entropia.de/GPN21), just before a joint bar shift by [@romses](https://chaos.social/@romses) and [@foosel](https://chaos.social/@foosel). 
  Slow parts of the shift as well as the drive back to the Rhein-Main-Area are spent discussing the idea. Romses registers a domain name.

2023-06-30
: romses and foosel meet up for a joint tinkering session. The first two mainboards are built. The Datenzwerg is alive!

2023-07-08
: Another joint tinkering session takes place. Another 8 mainboards are built. The Datenzwerg army is growing!

2023-07-23
: The basic infrastructure goes live. Sensors start to report to the official servers at [datagnome.de](https://datagnome.de).

2023-08-15 - 2023-08-19
: Planned Datenzwerg deployment at [CCCamp23](https://events.ccc.de/camp/2023/infos/).

## Credits & Thanks

The Datenzwerg was created by [@romses](https://chaos.social/@romses) and [@foosel](https://chaos.social/@foosel).

The Datenzwerg logo was created by D.B.

The Datenzwerg model files are based on [this "Garden Gnome" model](https://www.printables.com/model/260908-garden-gnome) by [Sci3D](https://www.printables.com/@Sci3D), released under CC-BY.


[^1]: Yes, the last three are not canon, and one of them even is a smurf - so what, chaos ftw!
[^2]: Prompt: 'Write me a text for a website that gives an overview of the "Datenzwerg". The Datenzwerg is a garden gnome that collects environmental data, and makes it publicly available. The Datenzwerg will be presented at the Chaos Communication Camp.'
