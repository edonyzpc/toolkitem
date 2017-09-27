<!--
<table>
<thead>
<tr>
<th align="center">Branchs</th>
<th align="center">CI</th>
<th align="center">Code Qulity</th>
<th align="center">Status</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><strong><i>[master]</strong></i></td>
<td align="center">[![Build Status](https://travis-ci.org/edonyM/toolkitem.svg?branch=master)](https://travis-ci.org/edonyM/toolkitem)</td>
<td align="center">[![codecov](https://codecov.io/gh/edonyM/toolkitem/branch/master/graph/badge.svg)](https://codecov.io/gh/edonyM/toolkitem)</td>
<td rowspan="3" align="center">![develop branch](https://codecov.io/gh/edonyM/toolkitem/branch/develop/graphs/sunburst.svg)<br><b><i>COVERAGE SUNBURST</i></b></br></td>
</tr>
<tr>
<td align="left"><strong><i>[develop]</i></strong></td>
<td align="center">[![Build Status](https://travis-ci.org/edonyM/toolkitem.svg?branch=develop)](https://travis-ci.org/edonyM/toolkitem)</td>
<td align="center">[![codecov](https://codecov.io/gh/edonyM/toolkitem/branch/develop/graph/badge.svg)](https://codecov.io/gh/edonyM/toolkitem)</td>
</tr>
<tr>
<td align="left"><strong><i>[publish]</i></strong></td>
<td align="center">[![Build Status](https://travis-ci.org/edonyM/toolkitem.svg?branch=publish)](https://travis-ci.org/edonyM/toolkitem)</td>
<td align="center">[![codecov](https://codecov.io/gh/edonyM/toolkitem/branch/publish/graph/badge.svg)](https://codecov.io/gh/edonyM/toolkitem)</td>
</tr>
<tr>
<td align="center"><strong><i>commits</i></strong></td>
<td colspan="3" align="center">![develop branch](https://codecov.io/gh/edonyM/toolkitem/branch/develop/graphs/commits.svg)</td></tr></tbody></table>
-->
<table>
<thead>
<tr>
<th align="center">Branchs</th>
<th align="center">CI</th>
<th align="center">Code Qulity</th>
<th align="center">Status</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><strong><i>[master]</i></strong></td>
<td align="center"><a href="https://travis-ci.org/edonyM/toolkitem"><img src="https://travis-ci.org/edonyM/toolkitem.svg?branch=master" alt="Build Status"></a></td>
<td align="center"><a href="https://codecov.io/gh/edonyM/toolkitem"><img src="https://codecov.io/gh/edonyM/toolkitem/branch/master/graph/badge.svg" alt="codecov"></a></td>
<td rowspan="3" align="center"><img src="https://codecov.io/gh/edonyM/toolkitem/branch/develop/graphs/sunburst.svg" alt="develop branch"><br><b><i>COVERAGE SUNBURST</i></b><br></td>
</tr>
<tr>
<td align="left"><strong><i>[develop]</i></strong></td>
<td align="center"><a href="https://travis-ci.org/edonyM/toolkitem"><img src="https://travis-ci.org/edonyM/toolkitem.svg?branch=develop" alt="Build Status"></a></td>
<td align="center"><a href="https://codecov.io/gh/edonyM/toolkitem"><img src="https://codecov.io/gh/edonyM/toolkitem/branch/develop/graph/badge.svg" alt="codecov"></a></td>
</tr>
<tr>
<td align="left"><strong><i>[publish]</i></strong></td>
<td align="center"><a href="https://travis-ci.org/edonyM/toolkitem"><img src="https://travis-ci.org/edonyM/toolkitem.svg?branch=publish" alt="Build Status"></a></td>
<td align="center"><a href="https://codecov.io/gh/edonyM/toolkitem"><img src="https://codecov.io/gh/edonyM/toolkitem/branch/publish/graph/badge.svg" alt="codecov"></a></td>
</tr>
<tr>
<td align="center"><strong><i>commits</i></strong></td>
<td colspan="3" align="center"><img src="https://codecov.io/gh/edonyM/toolkitem/branch/develop/graphs/commits.svg" alt="develop branch"></td></tr></tbody></table>


## toolkitem

----

### ***personal toolkits for daily code***

This is a toolkit project for speedup my daily life. It will be reconstituted into a GUI application if this project begins to take shape. According to daily requirements, it is split into different modules according to its functionality.

At the last but not least, these tools will be embedded into my big project [anth](https://github.com/edonyM/anth) (now an pre-research project), particularly, it is a qualified web crawler with high customizable walking purpose.

----

- FILE PROCESS TOOLS
    - [x] get all the directories and files in the root path and its sub-directories ====> `filesprocess/dirlist`
    - [x] count number of lines in direction files  ====>  `filesprocess/filesline`
    - [ ] mark up the files different lines(if they have) and write them into buffer  ====>  `mergefile`
    - [ ] delete syntax format(`*.md`,`*.rst` and so on) and get the plain text file.   ====>  `fileparser`
    - [ ] personal defined text handler for text process.  ====>  `texthandler`
- Git REPOS TOOLS
    - [x] git repository management tools. ====> `gitmgr`
- PYTHON FORMAT PRINT TOOLS
    - [x] make terminal standard output colorful. ====> `colorprinter`
    - [x] python progress bar simulating npm. ====> `spinner`
- SOURCE CODE MANAGEMENT TOOLS
    - [x] update system for preparation and update the git repositroies  ====>  `updatesys`
- MULTIPROCESS SPEEDUP TOOLS
    - [ ] multi-jobs running tools. ====> `scheduler`
- OTHER TOOLS
    - [x] Linux Kernel Integrity Measurement check tools. ====> `other/imacheck.py`
- TO BE DONE TOOLS
    - [ ] plan arangement in calendar  ====>  `plandaycal`
    - [ ] convert the `*.rst`, `*.md` and `*.txt` files into pdf  ====>  `pdfconvertor`
    - [ ] filter for files or directions search.  ====>  `fuzzyfinder`
    - [ ] personal Linux automatic management and efficient tools with Shell script.  ====> `emsh`
    - [ ] some awsome useful python script for daily working.  ====>  `pyscript`
    - [ ] resource of operation system monitor.  ====> `rosmonitor`
    - [ ] blog writing template generater tools and hexo management tools. ====> `blogger`
    - [ ] tools for cross developing with c and python. ====> `swiger`
    - [ ] auto reminder tools for checking new emails. ====> `mail`
- DEPLOY TOOLKITEM TO PYPI
    - [ ] deploy `spinner` to PyPi

### P.S.
------
[Develop Path](./DEVELOP.md)
