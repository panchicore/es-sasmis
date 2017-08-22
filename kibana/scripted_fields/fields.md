
#### sf_reported_within_days

Type: Number

```
(doc['report_date'].date.getMillis() - doc['incident_date_complete'].date.getMillis()) / 1000 / 60 / 60 / 24
```


#### sf_year

Type: Number

```
doc['incident_date_complete'].date.year
```


#### sf_wf_score100
Type:
Percentage

```
doc['wf_score'].value
```

#### sf_is_work_related_v2

Type: Boolean

```
if(doc['is_work_related'].value == true){ return true } else if (doc['has_wfp_victims'].value == true){ return true }else{ return false }
```



#### sf_month

Type: Number

```
doc['incident_date_complete'].date.getMonthOfYear()
```


#### sf_has_priority_victims

Type: Boolean

```
if (doc['has_wfp_victims'].value == true){ return true }else if (doc['has_contractor_victims'].value == true){ return true }else if (doc['has_partner_victims'].value == true){ return true }else{ return false }
```

