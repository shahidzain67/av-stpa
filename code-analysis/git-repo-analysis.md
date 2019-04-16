# Some quick analysis of Apollo codebase

Based on master as of 18th Oct 2018
(23b726544d268e969bca4a3955ca65c91cc4c84a)

In summary

- first public commit Tue Jul 4 12:04:34 2017
- sloccount with default cocomo parameters suggests 60 effort years
- git-active-days suggests 30 effort years since 1.0 release (which is a
  snapshot dump)
- commits are attributed to 269 unique emails (59 baidu emails) but many of
  these are obviously duplicates
- guesstimate approx 100 unique contributors in public (unkown how many in
  private led to 1.0)

So with some confidence we can say that:

- at least 100 people have worked on the Apollo codebase, from many
  organisations, and it is the result of more than 50 person-years of work

## sloccount

```
SLOC    Directory       SLOC-by-Language (Sorted)
217084  modules         cpp=181633,python=15330,ansic=11503,javascript=7696,
                        sh=922
7017    third_party     cpp=6924,ansic=93
2646    scripts         sh=2495,python=151
995     docker          sh=828,python=167
852     top_dir         sh=852
37      docs            python=37
5       tools           sh=5


Totals grouped by language (dominant language first):
cpp:         188557 (82.47%)
python:       15685 (6.86%)
ansic:        11596 (5.07%)
javascript:      7696 (3.37%)
sh:            5102 (2.23%)

Total Physical Source Lines of Code (SLOC)                = 228,636
Development Effort Estimate, Person-Years (Person-Months) = 60.00 (719.97)
 (Basic COCOMO model, Person-Months = 2.4 * (KSLOC**1.05))
Schedule Estimate, Years (Months)                         = 2.54 (30.46)
 (Basic COCOMO model, Months = 2.5 * (person-months**0.38))
Estimated Average Number of Developers (Effort/Schedule)  = 23.64
Total Estimated Cost to Develop                           = $ 8,104,822
 (average salary = $56,286/year, overhead = 2.40).
SLOCCount, Copyright (C) 2001-2004 David A. Wheeler
SLOCCount is Open Source Software/Free Software, licensed under the GNU GPL.
SLOCCount comes with ABSOLUTELY NO WARRANTY, and you are welcome to
redistribute it under certain conditions as specified by the GNU GPL license;
see the documentation for details.
Please credit this data as "generated using David A. Wheeler's 'SLOCCount'."
```

## research-git-active-days

Using code from [research-git-active-days](https://github.com/CodethinkLabs/research-git-active-days)

```
$ research-git-active-days/git-active-days --person-days --all-refs
3175
```

## release model and issue tracking

```
$ git tag

v1.0.0
v1.5.0
v2.0.0
v2.5.0
v3.0.0
```

So the project has done a small number of major releases. There seems to be no
model for offering updates to the releases.

Currently there are 319 issues open, 866 closed. There are 24 open pull requests,
4671 closed. This suggests that upstream is active on addressing issues and
accepting contributions.

All pull requests are run through travis-ci, which performs several steps:

```
    - JOB=lint
    - JOB=cibuild
    - JOB=citest_basic
    - JOB=citest_map
    - JOB=citest_dreamview
    - JOB=citest_perception
```

