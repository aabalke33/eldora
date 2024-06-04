package forms

import (
	"encoding/json"
	"fmt"
	"os"
	"strconv"
)

type field any

type Form interface {
	Build(onFile bool) (script string)
	GetTin() (payerTin field)
}

func FillForm(jsonPath string, form Form) {

	bytes, err := os.ReadFile(jsonPath)
	if err != nil {
		panic(err)
	}

	if err := json.Unmarshal(bytes, &form); err != nil {
		panic(err)
	}
}

func openFormEntryWindow(search, existEntryWin string) (script string) {

	script += fmt.Sprintf(
		`
        Sleep 2000
        Send "%s{Enter}"
        `, search)

	script += fmt.Sprintf(
		`
        Sleep 2000
        if WinActive("%s") {
            Send "{Enter}"
        } else {
            seekNewForm()
        }
        `, existEntryWin)

	script +=
		`
        Sleep 1000
        if !WinActive(userWin) {
            MsgBox "the Entry Box did not open"
            ExitApp
        }
        `

	return script
}

func fillEntryWindow(fields []field) (script string) {

	script += fmt.Sprintf("Send \"")

	for _, field := range fields {
		switch f := field.(type) {
		case string:
			script += f
		case int:
			script += strconv.Itoa(f)
		case bool:
			script += "{Space}"
		}

		script += "{Tab}"
	}

	return script
}

func closeFormEntryWindow() (script string) {

	script += "{Esc}\"\n"

	script += (`if !WinActive(userWin) {
            MsgBox "The entry page did not close properly"
            ExitApp
        }
        `)

	return script
}
