# Cars Fuel Efficiency: Benchmark Edition

This dataset contains enriched trip-level car fuel efficiency data, cleaned and enhanced for Kaggle projects.

## Columns

- trip\_id: Unique trip identifier  
- car\_name: Car model name  
- vehicle\_type: Type of vehicle  
- fuel\_type: Fuel type used  
- trip\_category: Category of trip  
- distance\_km: Trip distance (km)  
- trip\_duration\_hr: Trip duration (hours)  
- avg\_speed\_kmph: Average speed (km/h)  
- base\_mileage\_kmpl: Manufacturer mileage (km/l)  
- actual\_mileage\_kmpl: Observed mileage (km/l)  
- mileage\_delta\_kmpl: Difference between base and actual mileage  
- fuel\_consumed\_L: Fuel consumed (liters)  
- fuel\_cost\_usd: Total fuel cost (USD)  
- cost\_per\_km\_usd: Fuel cost per km (USD/km)  
- co2\_emissions\_kg: Total CO₂ emissions (kg)  
- co2\_per\_km: CO₂ emissions per km (kg/km)  
- relative\_efficiency: Relative efficiency score  
- efficiency\_band: Efficiency band classification  
- fuel\_efficiency\_ratio: Actual vs base mileage ratio  
- speed\_efficiency\_ratio: Average speed divided by actual mileage  
- cost\_to\_emission\_ratio: Fuel cost per unit CO₂ emitted  
- trip\_efficiency\_profile: Trip type classification (Urban, Mixed, Highway)  
- trip\_intensity: Distance divided by duration (km/h proxy)  
- efficiency\_class: Categorical efficiency rating (Low, Medium, High, Ultra)  
- benchmark\_flag: True if trip meets ideal efficiency criteria  
- outlier\_flag: True if trip is an outlier in mileage or emissions  
- data\_quality\_score: Score based on data completeness and plausibility

