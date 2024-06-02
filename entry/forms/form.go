package forms

import (
	"encoding/json"
	"fmt"
	"os"
)

type field string

type Form interface {
	Build(onFile bool) (script string)
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

	script += fmt.Sprintf("Send \"%s{Enter}\"\n", search)

	script += fmt.Sprintf(
		`
        Sleep 2000
        if WinExist("%s") {
            Send "{Enter}"
        } else {
            seekNewForm()
        }
        `, existEntryWin)

	script +=
		`if !WinExist(userWin) {
            MsgBox "the Entry Box did not open"
            ExitApp
        }
        `

	return script
}

func fillEntryWindow(fields []field) (script string) {

	script += fmt.Sprintf("Send \"")

	for _, field := range fields {
		script += string(field) + "{Tab}"
	}

	return script
}

func closeFormEntryWindow() (script string) {

	script += "{Esc}\"\n"

	script += (`if !WinExist(userWin) {
            MsgBox "The entry page did not close properly"
            ExitApp
        }
        `)

	return script
}
