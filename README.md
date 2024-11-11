## Commands:
#### Operation Commands
Syntax: `operation a b`<br>
any extra arguments after a and b will be ignored

`add a b`: outputs a + b<br>
`subtract a b`: outputs a - b<br>
`multiply a b`: outputs a * b<br>
`divide a b`: outputs a / b<br>

#### Non-Operation Commands
Syntax: `command`<br>
any extra arguments will be ignored

`help`: outputs a list of available commands<br>
`history`: outputs a list of previous calculations<br>
`clear`: clears the history<br>
`save`: stores the history in a csv file<br>
`load`: loads history from a csv file<br>
`exit`: saves history and exits program<br>

## Settings/Environment Variables
`HIST_PATH`: directory that history.csv will be saved<br>
`HIST_MAX`: max number of calculations stored in history<br>
