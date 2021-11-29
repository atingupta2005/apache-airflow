# Monitoring Apache Airflow

How does the logging system work in Airflow?

Setting up custom logging

Storing logs in Azure

Elasticsearch Overview

Configuring Airflow with Elasticsearch

Monitoring your DAGs with Elasticsearch

Introduction to metrics

Monitoring Airflow with TIG stack

Triggering alerts for Airflow with Grafana

Airflowmaintenance DAGs

# How the logging system works in Airflow

The logger system

# The basics

* Based on the logging module
* Written into files
* Log levels \(INFO\, ERROR\, DEBUG\, WARNING\, CRITICAL\)
* Formatters
* Handlers for outputs
  * FileHandIer
  * StreamHandler
  * NulIHandler

# How the logger is set up

* getLogger\(\)
* FileHandIer
* Formatter
  * settings\.SlMPLE\_LOG\_FORMAT
* setFormatter
* addHandIer
* setLeveI
  * settings\.LOGGlNG\_LEVEL

![](img/13-Monitoring%20Apache%20Airflow1.png)

# How the logging system works?

![](img/13-Monitoring%20Apache%20Airflow2.png)

# Where the logs are stored?

* Depends on the handler
  * File
  * Stream
  * S3
  * ES
  * GCS
  * …

# Elasticsearch Reminder

# What is Elasticsearch?

![](img/13-Monitoring%20Apache%20Airflow3.png)

# How Elasticsearch works?

  * <span style="color:#7030A0">\{</span>
  * <span style="color:#7030A0">"\_id": 2\,</span>
  * <span style="color:#7030A0">"Name": "</span>  <span style="color:#7030A0">my\_log</span>  <span style="color:#7030A0">"\,</span>
  * <span style="color:#7030A0">"Message": "it works"\,</span>
  * <span style="color:#7030A0">"</span>  <span style="color:#7030A0">LogLevel</span>  <span style="color:#7030A0">": " INFO" \,</span>
  * <span style="color:#7030A0">"Process": "ueryd\_8990"</span>
  * <span style="color:#7030A0">"\_type": "</span>  <span style="color:#7030A0">log\_sys</span>  <span style="color:#7030A0">"</span>
  * <span style="color:#7030A0">\}</span>

![](img/13-Monitoring%20Apache%20Airflow4.png)

![](img/13-Monitoring%20Apache%20Airflow5.png)

# ELK Stack

![](img/13-Monitoring%20Apache%20Airflow6.png)

# Configuring Airflow with Elasticsearch

Setting up the ELK architecture and Airflow

# Architecture

![](img/13-Monitoring%20Apache%20Airflow7.png)

![](img/13-Monitoring%20Apache%20Airflow8.png)

![](img/13-Monitoring%20Apache%20Airflow9.png)

# Important points

* Airflow assumes that each log message has the field offset
  * Number to read logs in the right order
  * Defined throughFilebeat
* Airflow assumes that each log message has the fieldlog\_id
  * \{dag\_id\}\-\{task\_id\}—\{execution\_date\}—\{try\_number\}
  * Must be defined through Logstash

# Introduction to metrics

Airflow andStatsD

# StatsD

Airflow sends metrics toStatsD

Daemon to aggregate and summarize application metrics

Extremely fast \(UDP\) and tiny resource footprint

Forward metrics to other applications

![](img/13-Monitoring%20Apache%20Airflow10.png)

# Metrics

* All metrics based on three types
  * Counters
  * Gauges
  * Timers
* Exhaustive lists
  * [https://airfiow\.apache\.org/docs/stabIe/metrics\.html](https://airfiow.apache.org/docs/stabIe/metrics.html)

# TIG Stack

* Telegraf
  * Agent for collecting\, processing\, aggregating metrics
* InfluxDB
  * Time series database
* Grafana
  * Data visualization and monitoring application

![](img/13-Monitoring%20Apache%20Airflow11.png)

# Important points

StatsDpackage must be installed

Metrics can be filtered withstatsd\_allow\_list

# Airflow Maintenance DAGs

![](img/13-Monitoring%20Apache%20Airflow12.png)

# Airflow Log Cleanup

![](img/13-Monitoring%20Apache%20Airflow13.png)

# Airflow DB Cleanup

![](img/13-Monitoring%20Apache%20Airflow14.png)

# Airflow Kill Halted Tasks

![](img/13-Monitoring%20Apache%20Airflow15.png)
