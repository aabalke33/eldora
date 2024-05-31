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

	output := fmt.Sprintf(`#Requires AutoHotkey >=2.0
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

    text := "`, drakeWin)

	//Need Method to handle multiple forms

	output += writeW2s([]string{
		"./data/w2.json",
		"./data/w2_2.json",
		"./data/w2_3.json",
	}, eins)
	output += "\"\n\nSend text"

	d1 := []byte(output)
	if err := os.WriteFile("w2s.ahk", d1, 0644); err != nil {
		panic(err)
	}

}

func writeW2s(files []string, eins ein.Eins) (output string) {

	for idx, file := range files {
		w2 := forms.W2{}
		forms.FillForm(file, &w2)
		if eins[string(w2.Ein)] {
			output += w2.Build(true, idx)
			continue
		}
		output += w2.Build(false, idx)
	}

	return output
}
