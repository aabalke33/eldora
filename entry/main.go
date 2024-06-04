package main

import (
	"eldora/entry/ein"
	"eldora/entry/forms"
	"fmt"
	"os"
)

type formType int

const (
	W2 formType = iota
	Int
	Div
	Retirement
	Ssa
	W2g
	G
)

func main() {

	eins := *ein.NewEins()
	eins.ReadDb()

	output := fmt.Sprintf(`
    #Requires AutoHotkey >=2.0

    userWin := "DRAKE 2023 - Data Entry (%d - %s, %s) - (CONTAINS SENSITIVE DATA)"

	seekNewForm() {
		A_Clipboard := ""
		Send "^c"
		ClipWait 1
		
		if A_Clipboard = "" {
			return
		}
		
		Send "{PgDn}{PgDn}"
		seekNewForm()	
	}

    /*
    Check if drake is open
    drakeWin := "a.txt - Notepad"
    */
    if WinExist(userWin) {
        WinActivate
    } else {
        MsgBox "Please Open Drake"
        ExitApp
    }
    `, user.SSN, user.LastName, user.FirstName)

	output += writeForms([]string{
		"./data/w2.json",
		"./data/w2_2.json",
		"./data/w2_3.json",
	}, eins, W2)

	output += writeForms([]string{
		"./data/int.json",
		"./data/int_2.json",
		"./data/int.json",
		"./data/int_2.json",
	}, eins, Int)

	output += writeForms([]string{
		"./data/div.json",
		"./data/div_2.json",
		"./data/div.json",
		"./data/div_2.json",
	}, eins, Div)

	output += writeForms([]string{
		"./data/retirement.json",
		"./data/retirement_2.json",
		"./data/retirement.json",
		"./data/retirement_2.json",
	}, eins, Retirement)

	output += writeForms([]string{
		"./data/ssa1.json",
		"./data/ssa2.json",
		"./data/ssa1.json",
		"./data/ssa2.json",
	}, eins, Ssa)

	output += writeForms([]string{
		"./data/w2g.json",
		"./data/w2g2.json",
		"./data/w2g.json",
		"./data/w2g2.json",
	}, eins, W2g)

	output += writeForms([]string{
		"./data/99g.json",
		"./data/99g2.json",
	}, eins, G)

	if err := os.WriteFile("output.ahk", []byte(output), 0644); err != nil {
		panic(err)
	}
}

func writeForms(files []string, eins ein.Eins, formType formType) (output string) {

	for _, file := range files {
		var form forms.Form
		switch formType {
		case W2:
			form = &forms.W2{}
		case Int:
			form = &forms.Int{}
		case Div:
			form = &forms.Div{}
		case Retirement:
			form = &forms.Retirement{}
		case Ssa:
			form = &forms.Ssa{}
		case W2g:
			form = &forms.W2g{}
		case G:
			form = &forms.G{}
		}

		forms.FillForm(file, form)

		ein := form.GetTin().(string)
		if eins.Eins[ein] {
			output += form.Build(true)
			continue
		}

		eins.Add(ein)
		output += form.Build(false)
	}

	return output
}
