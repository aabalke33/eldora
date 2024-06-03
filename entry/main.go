package main

import (
	"eldora/entry/ein"
	"eldora/entry/forms"
	"fmt"
	"os"
)

func main() {

	eins := ein.GetEins()

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

	output += writeW2s([]string{
		"./data/w2.json",
		"./data/w2_2.json",
		"./data/w2_3.json",
	}, eins)

	output += writeInts([]string{
		"./data/int.json",
		"./data/int_2.json",
		"./data/int.json",
		"./data/int_2.json",
	}, eins)

	output += writeDivs([]string{
		"./data/div.json",
		"./data/div_2.json",
		"./data/div.json",
		"./data/div_2.json",
	}, eins)

	output += writeRetirement([]string{
		"./data/retirement.json",
		"./data/retirement_2.json",
		"./data/retirement.json",
		"./data/retirement_2.json",
	}, eins)

	d1 := []byte(output)
	if err := os.WriteFile("output.ahk", d1, 0644); err != nil {
		panic(err)
	}
}

func writeW2s(files []string, eins ein.Eins) (output string) {

	for _, file := range files {
		w2 := forms.W2{}
		forms.FillForm(file, &w2)
		if eins[w2.PayerTin.(string)] {
			output += w2.Build(true)
			continue
		}
		output += w2.Build(false)
	}

	return output
}

func writeInts(files []string, eins ein.Eins) (output string) {

	for _, file := range files {
		int := forms.Int{}
		forms.FillForm(file, &int)
		if eins[int.PayerTIN.(string)] {
			output += int.Build(true)
			continue
		}
		output += int.Build(false)
	}

	return output
}

func writeDivs(files []string, eins ein.Eins) (output string) {

	for _, file := range files {
		div := forms.Div{}
		forms.FillForm(file, &div)
		if eins[div.PayerTIN.(string)] {
			output += div.Build(true)
			continue
		}
		output += div.Build(false)
	}

	return output
}

func writeRetirement(files []string, eins ein.Eins) (output string) {

	for _, file := range files {
		retirement := forms.Retirement{}
		forms.FillForm(file, &retirement)
		if eins[retirement.PayerTIN.(string)] {
			output += retirement.Build(true)
			continue
		}
		output += retirement.Build(false)
	}

	return output
}
