
I need regex patterns that match these strings:
`minutes` may be represented as:
`min`, `mins`, `minute`, `minutes`, `m`

`seconds` may be represented as:
`sec`, `secs`, `second`, `seconds`, `s`

`hours` may be represented as:
`hr`, `hrs`, `hour`, `hours`, `h`

`days` may be represented as:
`day`, `days`, `d`

`weeks` may be represented as:
`week`, `weeks`, `wk`, `wks`, `w`

`months` may be represented as:
`month`, `months`, `mo`, `mos`

`years` may be represented as:
`year`, `years`, `yr`, `yrs`, `y`

`am` may be represented as:
`a.m.`, `a.m`, `am`

`pm` may be represented as:
`p.m.`, `p.m`, `pm`

`midnight` may be represented as:
`midnight`, `midnite`, `mid nite`, `mid-nite`

there is also the possibility of encountering `unknown` or `unk` for any of the above time units.

On the values end of this regex I need to match the following:

people use the syntax `1-2` to mean `1` to `2` of something. These rows need to be assigned a different time value score than those that are most specific. Use a new column `duration value` for this and put the difference between the two values in the `duration` column. For example, if the duration is `1-2` then the `duration value` should be `1`. If the duration is `5-10` then the `duration value` should be `5`. At the end we will use MinMax scaling to normalize the values in the `duration value` column and use that in our analysis.

when you see `5-10` in the `duration (minutes/hrs)` column make the `calculated_duration` column the mean of the max and min of the two numbers in the provided range.

when you see `5 to 10`, `5 to ten`, `five` or any other form of these patterns calculate the mean and assign that to the `calculated_duration` column.