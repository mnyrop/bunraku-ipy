## POST-PANDAS PROCESSING

IF NEEDED:

`replace "[OLD STRING]" "[NEWSTRING]" -- [FILENAME]`

replace "[null]" "null" --
replace "\"nan\"" "null" --

<sup>(e.g. pesky `NaN`s to `null`s, or `[null]`s to `nulls`)</sub>

DROP NULLS:

`jq 'del(.[][] | nulls)' --compact-output [FILENAME] > [NEWFILENAME]`

CONVERT TO YAML

`python -c 'import sys, yaml, json; yaml.safe_dump(json.load(sys.stdin), sys.stdout, default_flow_style=False)' <  [JSONFILE] > [YAMLFILE]`
