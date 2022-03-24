The functionality to calculate day of week based on provided date.

* [Getting started](#getting-started)
  * [Introduction](#introduction)
  * [Technical stack](#technical-stack)
  * [Usage](#usage)
* [API](#api)
  * [Function](#function)
* [Development](#development)
  * [Clone the project](#clone-the-project)
* [Production](#production)
  * [Building](#building)

## Getting started

### Introduction

The functionality was created to get day of week name based on provided date.

### Technical stack

* [Python3](https://www.python.org/downloads) as an interpreter (programming language) to execute the code.
  * The following has been tested: `3.9`.

### Usage

Enter `Python3` interpreter and use the following code to save new AB test settings:

```python
>> from weekday import calc_weekday
>> day_of_week = calc_weekday('2022-03-24')
>> print(day_of_week)
Thursday
```

## API

### Function

Module provides one API function `cals_weekday` to get day of week name from provided date.

```python
>> from weekday import calc_weekday
>> day_of_week = calc_weekday('2022-03-24')
```

Arguments:

| Field    | Type    | Required | Restrictions         | Description |
|:--------:|:-------:|:--------:|:--------------------:|:-----------:|
| date_str | String  | Yes      | "YYYY-mm-dd" format. | Date value. |

Known errors

| Field    | Level                         | Error message                                                                              |
|:--------:|:-----------------------------:|--------------------------------------------------------------------------------------------|
| date_str | Incoming arguments validation | The provided arguments do not comply restrictions. Value should be in format "YYYY-mm-dd". |

## Development

### Clone the project

To clone the project, use the following command:

```bash
$ git clone git@github.com:andritar/week-day.git
$ cd week-day
```

Activate virtual environment if desired:

```bash
$ mkdir ~/.virtualenvs
$ virtualenv -p 3.9 ~/.virtualenvs/week-day
$ source ~/.virtualenvs/week-day/bin/activate
```

## Production

### Building

To build a project in a Python package, use the following command:

```bash
$ python3 setup.py sdist
```

To install the package, use the following command (be careful to install and use in the different folder than the
project as you may use project's modules instead of installed):

```bash
$ pip3 install dist/week-day-1.0.0.tar.gz
```
