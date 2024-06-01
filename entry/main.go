package main

import (
	"eldora/entry/ein"
	"eldora/entry/forms"
	"fmt"
	"os"
)

func main() {

	//This will have to be fixed so you don't call the read file every time
	eins := ein.GetEins()

	output := fmt.Sprintf(`
    #Requires AutoHotkey >=2.0
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
    drakeWin := "%s"
    if WinExist(drakeWin) {
        WinActivate
    } else {
        MsgBox "Please Open Drake"
        ExitApp
    }
    `, DrakeWin)

	//Need Method to handle multiple forms

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

	d1 := []byte(output)
	if err := os.WriteFile("output.ahk", d1, 0644); err != nil {
		panic(err)
	}

}

func writeW2s(files []string, eins ein.Eins) (output string) {

	for _, file := range files {
		w2 := forms.W2{}
		forms.FillForm(file, &w2)
		if eins[string(w2.Ein)] {
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
		if eins[string(int.PayerTIN)] {
			output += int.Build(true)
			continue
		}
		output += int.Build(false)
	}

	return output
}
