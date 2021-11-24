# Set Ubuntu Dates


- Set timezone to Europe/Amsterdam (UTC+1)
```
date
timedatectl
sudo timedatectl set-timezone Europe/Amsterdam
timedatectl
date
```


## Dates
```
sudo date --set "25 Sep 2013 15:00:00"
```


```
sudo timedatectl set-ntp false
```

```
sudo timedatectl set-ntp off
```

```
timedatectl
```


## Show hardware clock
```
sudo hwclock --show --verbose
```

## Set the System Time from the Hardware Clock.
```
sudo hwclock --hctosys
```


```
sudo date -s 'next year'
```


```
sudo date -s 'last year'
```


```
sudo date -s 'last month'
```


```
sudo date -s 'next month'
```

```
sudo date -s 'next day'
```


```
sudo date -s 'last day'
```

```
sudo date -s "+30 minutes"
```

```
sudo date -s "-30 minutes"
```

```
sudo timedatectl set-time 23:26:00
```

```
sudo timedatectl set-time YYYY-MM-DD
```
