# Merge Files Tool
------

Compare file1 with file2 to mark the difference. And fix the targeted file with interactive in vim editor.<br>

| Number  | TODO                                    |NOTE   |
|---------|:----------:                             |------:|
|**NO.1** |*read file1*                             |       |
|**NO.2** |*read file2, file2 is targeted file*     |       |
|**NO.3** |*write the marked difference into buffer*|       |
|**NO.4** |*read the buffer into vim editor*        |       |
|**NO.5** |*set fix or not flag in vim*             |       |
|**NO.6** |*update the targeted file*               |       |

> file read/write with ```python```

> vim flag setting with ```VimL```

> communication with ```python``` and ```VimL``` is bash
